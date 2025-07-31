#!/usr/bin/env python3
"""
Astraeus 系统监控脚本
实时监控系统运行状态
"""

import asyncio
import time
import sqlite3
from datetime import datetime, timedelta
from pathlib import Path

def print_header(title):
    """打印标题"""
    print(f"\n{'='*60}")
    print(f"📊 {title}")
    print(f"{'='*60}")

def get_system_status():
    """获取系统状态"""
    try:
        # 检查数据库
        db_path = Path("trading_system.db")
        if not db_path.exists():
            return "❌ 数据库文件不存在"
        
        conn = sqlite3.connect("trading_system.db")
        cursor = conn.cursor()
        
        # 检查资产数量
        cursor.execute("SELECT COUNT(*) FROM assets;")
        asset_count = cursor.fetchone()[0]
        
        # 检查价格记录
        cursor.execute("SELECT COUNT(*) FROM prices;")
        price_count = cursor.fetchone()[0]
        
        # 检查最新价格更新时间
        cursor.execute("SELECT MAX(timestamp) FROM prices;")
        latest_price = cursor.fetchone()[0]
        
        # 检查分析记录
        try:
            cursor.execute("SELECT COUNT(*) FROM analysis;")
            analysis_count = cursor.fetchone()[0]
            
            cursor.execute("SELECT MAX(timestamp) FROM analysis;")
            latest_analysis = cursor.fetchone()[0]
        except sqlite3.OperationalError:
            analysis_count = 0
            latest_analysis = None
        
        conn.close()
        
        # 计算时间差
        now = datetime.now()
        price_age = "未知"
        analysis_age = "未知"
        
        if latest_price:
            price_time = datetime.fromisoformat(latest_price.replace('Z', '+00:00'))
            price_age = str(now - price_time).split('.')[0]
        
        if latest_analysis:
            analysis_time = datetime.fromisoformat(latest_analysis.replace('Z', '+00:00'))
            analysis_age = str(now - analysis_time).split('.')[0]
        
        return {
            "status": "✅ 运行中",
            "assets": asset_count,
            "prices": price_count,
            "price_age": price_age,
            "analysis": analysis_count,
            "analysis_age": analysis_age
        }
        
    except Exception as e:
        return f"❌ 系统状态检查失败: {e}"

def get_top_assets():
    """获取热门资产"""
    try:
        conn = sqlite3.connect("trading_system.db")
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT symbol, price, market_cap, updated_at 
            FROM assets 
            WHERE is_active = 1 
            ORDER BY market_cap DESC 
            LIMIT 5
        """)
        
        assets = cursor.fetchall()
        conn.close()
        
        return assets
        
    except Exception as e:
        return []

def get_recent_activity():
    """获取最近活动"""
    try:
        conn = sqlite3.connect("trading_system.db")
        cursor = conn.cursor()
        
        # 获取最近的价格更新
        cursor.execute("""
            SELECT a.symbol, p.close_price, p.timestamp
            FROM prices p
            JOIN assets a ON p.asset_id = a.id
            ORDER BY p.timestamp DESC
            LIMIT 5
        """)
        
        recent_prices = cursor.fetchall()
        
        # 获取最近的分析
        try:
            cursor.execute("""
                SELECT a.symbol, an.signal_type, an.signal_strength, an.timestamp
                FROM analysis an
                JOIN assets a ON an.asset_id = a.id
                ORDER BY an.timestamp DESC
                LIMIT 5
            """)
            
            recent_analysis = cursor.fetchall()
        except sqlite3.OperationalError:
            recent_analysis = []
        
        conn.close()
        
        return recent_prices, recent_analysis
        
    except Exception as e:
        return [], []

async def main():
    """主监控函数"""
    print("🚀 Astraeus 系统监控")
    print("按 Ctrl+C 停止监控")
    print()
    
    try:
        while True:
            # 清屏
            print("\033[2J\033[H", end="")
            
            print_header("系统状态")
            status = get_system_status()
            
            if isinstance(status, dict):
                print(f"状态: {status['status']}")
                print(f"资产数量: {status['assets']}")
                print(f"价格记录: {status['prices']}")
                print(f"最新价格更新: {status['price_age']} 前")
                print(f"分析记录: {status['analysis']}")
                print(f"最新分析: {status['analysis_age']} 前")
            else:
                print(status)
            
            print_header("热门资产")
            assets = get_top_assets()
            if assets:
                print(f"{'符号':<8} {'价格':<12} {'市值':<15} {'更新时间'}")
                print("-" * 50)
                for symbol, price, market_cap, updated_at in assets:
                    price_str = f"${price:.4f}" if price else "N/A"
                    market_cap_str = f"${market_cap/1e9:.1f}B" if market_cap else "N/A"
                    updated_str = updated_at[:19] if updated_at else "N/A"
                    print(f"{symbol:<8} {price_str:<12} {market_cap_str:<15} {updated_str}")
            else:
                print("暂无资产数据")
            
            print_header("最近活动")
            recent_prices, recent_analysis = get_recent_activity()
            
            if recent_prices:
                print("📊 最新价格更新:")
                for symbol, price, timestamp in recent_prices:
                    time_str = timestamp[:19] if timestamp else "N/A"
                    print(f"  {symbol}: ${price:.4f} ({time_str})")
            
            if recent_analysis:
                print("\n📈 最新分析结果:")
                for symbol, signal, strength, timestamp in recent_analysis:
                    time_str = timestamp[:19] if timestamp else "N/A"
                    signal_emoji = "🟢" if signal == "BUY" else "🔴" if signal == "SELL" else "🟡"
                    print(f"  {signal_emoji} {symbol}: {signal} (强度: {strength:.2f}) ({time_str})")
            
            print_header("监控信息")
            print(f"⏰ 当前时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print("💡 提示: 系统每5分钟更新数据，每10分钟进行分析")
            print("📱 使用Telegram命令 /status 查看详细状态")
            
            # 等待30秒
            await asyncio.sleep(30)
            
    except KeyboardInterrupt:
        print("\n\n⏹️  监控已停止")
    except Exception as e:
        print(f"\n❌ 监控过程中发生错误: {e}")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n⏹️  监控被用户中断")
    except Exception as e:
        print(f"\n❌ 监控启动失败: {e}") 