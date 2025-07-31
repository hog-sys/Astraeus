"""
Astraeus 核心功能测试
测试配置、数据库和基本模块
"""

import sys
import os
from pathlib import Path

# 添加src目录到Python路径
sys.path.append(str(Path(__file__).parent / "src"))

def test_config_import():
    """测试配置模块导入"""
    print("🔧 测试配置模块...")
    try:
        from src.config.settings import config
        print("✅ 配置模块导入成功")
        
        # 测试配置获取
        config_dict = config.get_config_dict()
        print(f"✅ 配置加载成功，包含 {len(config_dict)} 个配置节")
        
        return True
    except Exception as e:
        print(f"❌ 配置模块测试失败: {e}")
        return False

def test_database_import():
    """测试数据库模块导入"""
    print("🗄️ 测试数据库模块...")
    try:
        from src.database.manager import db_manager
        from src.database.models import Base, Asset, Price, Trade, Position
        print("✅ 数据库模块导入成功")
        
        # 测试数据库初始化
        db_manager.initialize()
        print("✅ 数据库初始化成功")
        
        return True
    except Exception as e:
        print(f"❌ 数据库模块测试失败: {e}")
        return False

def test_data_providers_import():
    """测试数据提供者模块导入"""
    print("📊 测试数据提供者模块...")
    try:
        from src.data.providers import data_aggregator, CoinGeckoProvider
        print("✅ 数据提供者模块导入成功")
        
        # 测试CoinGecko提供者
        coingecko = CoinGeckoProvider()
        print("✅ CoinGecko提供者创建成功")
        
        return True
    except Exception as e:
        print(f"❌ 数据提供者模块测试失败: {e}")
        return False

def test_analysis_import():
    """测试分析引擎模块导入"""
    print("🧠 测试分析引擎模块...")
    try:
        from src.analysis.engine import analysis_engine, AnalysisResult
        print("✅ 分析引擎模块导入成功")
        
        return True
    except Exception as e:
        print(f"❌ 分析引擎模块测试失败: {e}")
        return False

def test_risk_import():
    """测试风险管理模块导入"""
    print("🛡️ 测试风险管理模块...")
    try:
        from src.risk.manager import risk_manager, PositionSizingResult
        print("✅ 风险管理模块导入成功")
        
        return True
    except Exception as e:
        print(f"❌ 风险管理模块测试失败: {e}")
        return False

def test_trading_import():
    """测试交易执行模块导入"""
    print("💹 测试交易执行模块...")
    try:
        from src.trading.executor import trading_executor, BinanceExecutor
        print("✅ 交易执行模块导入成功")
        
        return True
    except Exception as e:
        print(f"❌ 交易执行模块测试失败: {e}")
        return False

def test_notifications_import():
    """测试通知模块导入"""
    print("📱 测试通知模块...")
    try:
        from src.notifications.telegram import telegram_notifier
        print("✅ 通知模块导入成功")
        
        return True
    except Exception as e:
        print(f"❌ 通知模块测试失败: {e}")
        return False

def test_scheduler_import():
    """测试调度器模块导入"""
    print("⏰ 测试调度器模块...")
    try:
        from src.scheduler.automation import automation_scheduler
        print("✅ 调度器模块导入成功")
        
        return True
    except Exception as e:
        print(f"❌ 调度器模块测试失败: {e}")
        return False

def run_all_tests():
    """运行所有核心测试"""
    print("🚀 开始 Astraeus 核心功能测试...\n")
    
    tests = [
        ("配置模块", test_config_import),
        ("数据库模块", test_database_import),
        ("数据提供者", test_data_providers_import),
        ("分析引擎", test_analysis_import),
        ("风险管理", test_risk_import),
        ("交易执行", test_trading_import),
        ("通知模块", test_notifications_import),
        ("调度器模块", test_scheduler_import)
    ]
    
    results = []
    
    for test_name, test_func in tests:
        print(f"\n{'='*50}")
        print(f"测试: {test_name}")
        print('='*50)
        
        try:
            success = test_func()
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
        print("🎉 所有核心功能测试通过！")
        print("\n📋 系统状态:")
        print("✅ 所有模块可以正常导入")
        print("✅ 数据库连接正常")
        print("✅ 配置系统工作正常")
        print("✅ 可以启动Astraeus系统")
        print("\n💡 下一步:")
        print("1. 配置环境变量 (.env文件)")
        print("2. 启动系统: python main.py")
    else:
        print("⚠️ 部分模块测试失败，请检查依赖安装。")
        print("\n💡 建议:")
        print("1. 安装缺失的依赖: pip install -r requirements.txt")
        print("2. 检查Python环境")
    
    return passed == total

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1) 