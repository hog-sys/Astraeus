#!/usr/bin/env python3
"""
Astraeus 系统状态检查
快速查看系统当前状态
"""

import asyncio
import sqlite3
from datetime import datetime
from pathlib import Path

def print_header(title):
    """打印标题"""
    print(f"\n{'='*50}")
    print(f"📊 {title}")
    print(f"{'='*50}")

def check_config():
    """检查配置状态"""
    print_header("配置状态")
    
    try:
        from src.config.settings import config
        
        print(f"✅ 配置加载: 正常")
        print(f"🔑 Binance API: {'已配置' if config.api.binance_api_key else '未配置'}")
        print(f"📱 Telegram Bot: {'已配置' if config.api.telegram_bot_token else '未配置'}")
        print(f"💰 单日最大部署: {config.trading.max_daily_deployment_usdc} USDC")
        print(f"📈 最大并发持仓: {config.trading.max_concurrent_positions}")
        print(f"🛡️  默认止损: {config.trading.default_stop_loss_percent}%")
        print(f"🎯 默认止盈: {config.trading.default_take_profit_percent}%")
        
    except Exception as e:
        print(f"❌ 配置检查失败: {e}")

def check_database():
    """检查数据库状态"""
    print_header("数据库状态")
    
    db_path = Path("trading_system.db")
    if not db_path.exists():
        print("❌ 数据库文件不存在")
        return
    
    try:
        conn = sqlite3.connect("trading_system.db")
        cursor = conn.cursor()
        
        # 检查表结构
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        print(f"✅ 数据库文件: {db_path.name}")
        print(f"📋 数据表数量: {len(tables)}")
        
        # 检查资产数量
        cursor.execute("SELECT COUNT(*) FROM assets;")
        asset_count = cursor.fetchone()[0]
        print(f"💎 资产数量: {asset_count}")
        
        # 检查价格记录
        cursor.execute("SELECT COUNT(*) FROM prices;")
        price_count = cursor.fetchone()[0]
        print(f"📊 价格记录: {price_count}")
        
        # 检查交易记录
        cursor.execute("SELECT COUNT(*) FROM trades;")
        trade_count = cursor.fetchone()[0]
        print(f"🔄 交易记录: {trade_count}")
        
        # 检查持仓
        try:
            cursor.execute("SELECT COUNT(*) FROM positions WHERE status = 'ACTIVE';")
            active_positions = cursor.fetchone()[0]
            print(f"📈 活跃持仓: {active_positions}")
        except sqlite3.OperationalError:
            print("📈 活跃持仓: 表结构不完整")
        
        conn.close()
        
    except Exception as e:
        print(f"❌ 数据库检查失败: {e}")

async def check_data_sources():
    """检查数据源状态"""
    print_header("数据源状态")
    
    try:
        from src.data.providers import data_aggregator
        
        # 测试CoinGecko
        try:
            market_data = await data_aggregator.coingecko.get_market_data(per_page=1)
            if market_data:
                print("✅ CoinGecko: 连接正常")
            else:
                print("⚠️  CoinGecko: 连接异常")
        except Exception as e:
            print(f"❌ CoinGecko: 连接失败 - {e}")
        
        # 测试Binance
        try:
            ticker = await data_aggregator.binance.get_ticker_24h("BTCUSDT")
            if ticker:
                print("✅ Binance: 连接正常")
            else:
                print("⚠️  Binance: 连接异常")
        except Exception as e:
            print(f"❌ Binance: 连接失败 - {e}")
            
    except Exception as e:
        print(f"❌ 数据源检查失败: {e}")

def check_logs():
    """检查日志文件"""
    print_header("日志状态")
    
    log_files = ["astraeus.log", "error.log", "trades.log"]
    
    for log_file in log_files:
        log_path = Path(log_file)
        if log_path.exists():
            size = log_path.stat().st_size
            modified = datetime.fromtimestamp(log_path.stat().st_mtime)
            print(f"✅ {log_file}: {size} bytes, 修改时间: {modified.strftime('%Y-%m-%d %H:%M:%S')}")
        else:
            print(f"⚠️  {log_file}: 文件不存在")

def check_system_status():
    """检查系统状态"""
    print_header("系统状态")
    
    try:
        from src.database.manager import db_manager
        from src.database.models import SystemStatus
        
        # 获取最新系统状态
        session = db_manager.get_session()
        latest_status = session.query(SystemStatus).order_by(SystemStatus.timestamp.desc()).first()
        
        if latest_status:
            print(f"🕐 最后更新: {latest_status.timestamp}")
            print(f"📊 系统状态: {latest_status.status}")
            print(f"💾 内存使用: {latest_status.memory_usage} MB")
            print(f"🔄 活跃任务: {latest_status.active_tasks}")
        else:
            print("⚠️  无系统状态记录")
            
        session.close()
        
    except Exception as e:
        print(f"❌ 系统状态检查失败: {e}")

async def main():
    """主函数"""
    print("🚀 Astraeus 系统状态检查")
    print(f"⏰ 检查时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    check_config()
    check_database()
    await check_data_sources()
    check_logs()
    check_system_status()
    
    print_header("检查完成")
    print("💡 提示:")
    print("   - 使用 'python main.py' 启动系统")
    print("   - 使用 'python test_quick.py' 进行完整测试")
    print("   - 查看日志文件获取详细信息")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n⏹️  检查被用户中断")
    except Exception as e:
        print(f"\n❌ 检查过程中发生错误: {e}") 