"""
Astraeus 系统测试脚本
验证各个模块的功能
"""

import asyncio
import sys
from pathlib import Path

# 添加src目录到Python路径
sys.path.append(str(Path(__file__).parent / "src"))

from src.config.settings import config
from src.database.manager import db_manager
from src.data.providers import data_aggregator
from src.analysis.engine import analysis_engine
from src.risk.manager import risk_manager
from src.trading.executor import trading_executor
from src.notifications.telegram import telegram_notifier


async def test_config():
    """测试配置模块"""
    print("🔧 测试配置模块...")
    try:
        config_dict = config.get_config_dict()
        print(f"✅ 配置加载成功，包含 {len(config_dict)} 个配置节")
        return True
    except Exception as e:
        print(f"❌ 配置测试失败: {e}")
        return False


async def test_database():
    """测试数据库模块"""
    print("🗄️ 测试数据库模块...")
    try:
        db_manager.initialize()
        
        # 测试连接
        if db_manager.test_connection():
            print("✅ 数据库连接成功")
        else:
            print("❌ 数据库连接失败")
            return False
        
        # 获取数据库信息
        db_info = db_manager.get_database_info()
        print(f"✅ 数据库信息: {db_info['status']}")
        
        return True
    except Exception as e:
        print(f"❌ 数据库测试失败: {e}")
        return False


async def test_data_providers():
    """测试数据提供者"""
    print("📊 测试数据提供者...")
    try:
        # 测试获取市值排名
        top_assets = await data_aggregator.get_top_market_cap_assets(limit=5)
        print(f"✅ 获取到 {len(top_assets)} 个资产数据")
        
        if top_assets:
            print(f"   示例: {top_assets[0]['symbol']} - ${top_assets[0]['price']}")
        
        return True
    except Exception as e:
        print(f"❌ 数据提供者测试失败: {e}")
        return False


async def test_analysis_engine():
    """测试分析引擎"""
    print("🧠 测试分析引擎...")
    try:
        # 创建测试资产
        from src.database.models import Asset
        
        test_asset = Asset(
            symbol="BTC",
            name="Bitcoin",
            asset_type="CRYPTO",
            market_cap=1000000000000,  # 1万亿
            volume_24h=50000000000,    # 500亿
            price=50000,
            price_change_24h=2.5,
            is_active=True
        )
        
        # 测试分析
        analysis_result = await analysis_engine.analyze_asset(test_asset)
        
        if analysis_result:
            print(f"✅ 分析完成: 综合评分 {analysis_result.overall_score:.3f}")
            print(f"   信号类型: {analysis_result.signal_type}")
            print(f"   信号强度: {analysis_result.signal_strength:.3f}")
        else:
            print("⚠️ 分析结果为空（可能是缺少价格数据）")
        
        return True
    except Exception as e:
        print(f"❌ 分析引擎测试失败: {e}")
        return False


async def test_risk_manager():
    """测试风险管理器"""
    print("🛡️ 测试风险管理器...")
    try:
        # 测试投资组合风险评估
        portfolio_metrics = await risk_manager.assess_portfolio_risk()
        print(f"✅ 风险评估完成")
        print(f"   总价值: ${portfolio_metrics.total_value:,.2f}")
        print(f"   总盈亏: ${portfolio_metrics.total_pnl:,.2f}")
        print(f"   投资组合VaR: ${portfolio_metrics.portfolio_var:,.2f}")
        
        # 测试风险报告
        risk_report = await risk_manager.get_risk_report()
        print(f"✅ 风险报告生成完成")
        
        return True
    except Exception as e:
        print(f"❌ 风险管理器测试失败: {e}")
        return False


async def test_trading_executor():
    """测试交易执行器"""
    print("💹 测试交易执行器...")
    try:
        # 测试交易摘要
        trading_summary = await trading_executor.get_trading_summary()
        print(f"✅ 交易摘要生成完成")
        print(f"   活跃持仓: {trading_summary.get('active_positions', 0)} 个")
        print(f"   今日交易: {trading_summary.get('total_trades', 0)} 笔")
        
        return True
    except Exception as e:
        print(f"❌ 交易执行器测试失败: {e}")
        return False


async def test_notifications():
    """测试通知服务"""
    print("📱 测试通知服务...")
    try:
        # 测试发送通知（如果配置了Telegram）
        if config.api.telegram_bot_token and config.api.telegram_chat_id:
            await telegram_notifier.send_notification("🧪 系统测试通知")
            print("✅ 通知发送成功")
        else:
            print("⚠️ Telegram未配置，跳过通知测试")
        
        return True
    except Exception as e:
        print(f"❌ 通知服务测试失败: {e}")
        return False


async def run_all_tests():
    """运行所有测试"""
    print("🚀 开始 Astraeus 系统测试...\n")
    
    tests = [
        ("配置模块", test_config),
        ("数据库模块", test_database),
        ("数据提供者", test_data_providers),
        ("分析引擎", test_analysis_engine),
        ("风险管理器", test_risk_manager),
        ("交易执行器", test_trading_executor),
        ("通知服务", test_notifications),
    ]
    
    results = []
    
    for test_name, test_func in tests:
        print(f"\n{'='*50}")
        print(f"测试: {test_name}")
        print('='*50)
        
        try:
            success = await test_func()
            results.append((test_name, success))
        except Exception as e:
            print(f"❌ 测试异常: {e}")
            results.append((test_name, False))
    
    # 输出测试结果
    print(f"\n{'='*50}")
    print("📊 测试结果汇总")
    print('='*50)
    
    passed = 0
    total = len(results)
    
    for test_name, success in results:
        status = "✅ 通过" if success else "❌ 失败"
        print(f"{test_name:<20} {status}")
        if success:
            passed += 1
    
    print(f"\n总计: {passed}/{total} 个测试通过")
    
    if passed == total:
        print("🎉 所有测试通过！系统准备就绪。")
    else:
        print("⚠️ 部分测试失败，请检查配置和依赖。")
    
    return passed == total


if __name__ == "__main__":
    # 创建日志目录
    Path("logs").mkdir(exist_ok=True)
    
    # 运行测试
    success = asyncio.run(run_all_tests())
    
    # 退出码
    sys.exit(0 if success else 1) 