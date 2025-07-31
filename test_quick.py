#!/usr/bin/env python3
"""
Astraeus 快速测试脚本
验证系统基本功能是否正常
"""

import asyncio
import sys
from pathlib import Path

def print_status(message, status="INFO"):
    """打印状态信息"""
    if status == "SUCCESS":
        print(f"✅ {message}")
    elif status == "ERROR":
        print(f"❌ {message}")
    elif status == "WARNING":
        print(f"⚠️  {message}")
    else:
        print(f"ℹ️  {message}")

def test_imports():
    """测试基本导入"""
    print_status("测试基本模块导入...")
    
    try:
        import asyncio
        import aiohttp
        import pandas
        import numpy
        import loguru
        import pydantic_settings
        import sqlalchemy
        import ta
        print_status("基本模块导入成功", "SUCCESS")
        return True
    except ImportError as e:
        print_status(f"模块导入失败: {e}", "ERROR")
        return False

def test_config():
    """测试配置加载"""
    print_status("测试配置加载...")
    
    try:
        from src.config.settings import config
        print_status("配置加载成功", "SUCCESS")
        
        # 检查关键配置
        if config.api.binance_api_key:
            print_status("Binance API已配置", "SUCCESS")
        else:
            print_status("Binance API未配置", "WARNING")
            
        if config.api.telegram_bot_token:
            print_status("Telegram Bot已配置", "SUCCESS")
        else:
            print_status("Telegram Bot未配置", "WARNING")
            
        return True
    except Exception as e:
        print_status(f"配置加载失败: {e}", "ERROR")
        return False

async def test_database():
    """测试数据库连接"""
    print_status("测试数据库连接...")
    
    try:
        from src.database.manager import db_manager
        db_manager.initialize()  # 移除await，因为initialize不是异步函数
        print_status("数据库连接成功", "SUCCESS")
        return True
    except Exception as e:
        print_status(f"数据库连接失败: {e}", "ERROR")
        return False

async def test_data_providers():
    """测试数据提供者"""
    print_status("测试数据提供者...")
    
    try:
        from src.data.providers import data_aggregator
        
        # 测试CoinGecko
        market_data = await data_aggregator.coingecko.get_market_data(per_page=5)
        if market_data:
            print_status(f"CoinGecko连接成功，获取到{len(market_data)}个资产", "SUCCESS")
        else:
            print_status("CoinGecko连接失败", "WARNING")
            
        return True
    except Exception as e:
        print_status(f"数据提供者测试失败: {e}", "WARNING")
        return False

def test_analysis_engine():
    """测试分析引擎"""
    print_status("测试分析引擎...")
    
    try:
        from src.analysis.engine import AnalysisEngine
        engine = AnalysisEngine()
        print_status("分析引擎初始化成功", "SUCCESS")
        return True
    except Exception as e:
        print_status(f"分析引擎测试失败: {e}", "ERROR")
        return False

def test_risk_manager():
    """测试风险管理"""
    print_status("测试风险管理...")
    
    try:
        from src.risk.manager import RiskManager
        risk_manager = RiskManager()
        print_status("风险管理初始化成功", "SUCCESS")
        return True
    except Exception as e:
        print_status(f"风险管理测试失败: {e}", "ERROR")
        return False

async def main():
    """主测试函数"""
    print("=" * 50)
    print("🚀 Astraeus 系统快速测试")
    print("=" * 50)
    print()
    
    tests = [
        ("基本模块导入", test_imports),
        ("配置加载", test_config),
        ("数据库连接", test_database),
        ("数据提供者", test_data_providers),
        ("分析引擎", test_analysis_engine),
        ("风险管理", test_risk_manager),
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n📋 {test_name}")
        print("-" * 30)
        
        try:
            if asyncio.iscoroutinefunction(test_func):
                result = await test_func()
            else:
                result = test_func()
                
            if result:
                passed += 1
        except Exception as e:
            print_status(f"测试异常: {e}", "ERROR")
    
    print("\n" + "=" * 50)
    print(f"📊 测试结果: {passed}/{total} 通过")
    
    if passed == total:
        print_status("🎉 所有测试通过！系统可以正常启动", "SUCCESS")
        print("\n💡 启动系统:")
        print("   python main.py")
        print("   或使用启动脚本:")
        print("   Windows: launch.bat")
        print("   Linux/Mac: ./launch.sh")
    else:
        print_status("⚠️  部分测试失败，请检查配置和依赖", "WARNING")
        print("\n🔧 故障排除:")
        print("   1. 检查依赖安装: pip install -r requirements.txt")
        print("   2. 检查配置文件: .env")
        print("   3. 检查网络连接")
        print("   4. 查看详细日志")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n⏹️  测试被用户中断")
    except Exception as e:
        print(f"\n❌ 测试过程中发生错误: {e}")
        sys.exit(1) 