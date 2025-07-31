#!/usr/bin/env python3
"""
Astraeus 快速启动脚本
简化版部署和启动工具
"""

import os
import sys
import subprocess
from pathlib import Path

def print_header():
    print("🚀 Astraeus 快速启动")
    print("=" * 40)

def check_requirements():
    """检查基本要求"""
    print("📋 检查系统要求...")
    
    # 检查Python版本
    if sys.version_info < (3, 8):
        print("❌ 需要Python 3.8或更高版本")
        return False
    
    # 检查必要文件
    required_files = ["requirements.txt", "main.py", "src/"]
    for file in required_files:
        if not Path(file).exists():
            print(f"❌ 缺少必要文件: {file}")
            return False
    
    print("✅ 系统要求检查通过")
    return True

def setup_environment():
    """设置环境"""
    print("\n🔧 设置环境...")
    
    # 创建虚拟环境
    if not Path("venv").exists():
        print("创建虚拟环境...")
        subprocess.run([sys.executable, "-m", "venv", "venv"])
    
    # 激活虚拟环境并安装依赖
    if os.name == 'nt':  # Windows
        python_exe = "venv\\Scripts\\python.exe"
        pip_exe = "venv\\Scripts\\pip.exe"
    else:  # Unix/Linux/macOS
        python_exe = "venv/bin/python"
        pip_exe = "venv/bin/pip"
    
    # 安装依赖
    print("安装依赖...")
    subprocess.run([pip_exe, "install", "-r", "requirements.txt"])
    
    print("✅ 环境设置完成")
    return python_exe

def create_env_file():
    """创建环境配置文件"""
    if Path(".env").exists():
        print("✅ .env文件已存在")
        return True
    
    print("创建.env配置文件...")
    env_content = """# Astraeus 环境配置
# 请填入您的实际API密钥

# Binance API
BINANCE_API_KEY=your_binance_api_key_here
BINANCE_SECRET_KEY=your_binance_secret_key_here
BINANCE_TESTNET=true

# Telegram Bot
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
TELEGRAM_CHAT_ID=your_telegram_chat_id_here

# 系统配置
DATABASE_URL=sqlite:///trading_system.db
LOG_LEVEL=INFO

# 交易配置
MAX_DAILY_DEPLOYMENT_USDC=100
MAX_CONCURRENT_POSITIONS=3
DEFAULT_STOP_LOSS_PERCENT=2.0
DEFAULT_TAKE_PROFIT_PERCENT=6.0
RISK_PER_TRADE_PERCENT=1.0

# 分析配置
TECHNICAL_ANALYSIS_WEIGHT=0.4
FUNDAMENTAL_ANALYSIS_WEIGHT=0.4
SENTIMENT_ANALYSIS_WEIGHT=0.2

# 调度配置
DATA_UPDATE_INTERVAL_MINUTES=5
ANALYSIS_INTERVAL_MINUTES=10
PORTFOLIO_REBALANCE_INTERVAL_HOURS=24

# 风险控制
MAX_PORTFOLIO_VAR_PERCENT=5.0
BLACK_SWAN_VOLATILITY_THRESHOLD=50.0
"""
    
    with open(".env", "w", encoding="utf-8") as f:
        f.write(env_content)
    
    print("✅ .env文件创建完成")
    print("⚠️  请编辑.env文件，填入您的API密钥")
    return True

def show_config_guide():
    """显示配置指南"""
    print("\n" + "=" * 50)
    print("📝 配置指南")
    print("=" * 50)
    print()
    print("1. 🔑 Binance API设置:")
    print("   - 登录 https://www.binance.com")
    print("   - 进入 API管理 → 创建API")
    print("   - 设置权限: 现货交易 + 读取信息")
    print("   - 复制 API Key 和 Secret Key")
    print()
    print("2. 📱 Telegram Bot设置:")
    print("   - 在Telegram中搜索 @BotFather")
    print("   - 发送 /newbot 创建机器人")
    print("   - 记录 Bot Token")
    print("   - 获取 Chat ID: 与机器人对话后访问")
    print("     https://api.telegram.org/bot<TOKEN>/getUpdates")
    print()
    print("3. ⚙️ 编辑配置文件:")
    print("   - 打开 .env 文件")
    print("   - 填入您的实际API密钥")
    print("   - 保存文件")
    print()
    print("4. 🚀 启动系统:")
    print("   python main.py")
    print()
    print("5. 📱 测试Telegram控制:")
    print("   - 向机器人发送 /status")
    print("   - 发送 /help 查看命令")
    print("=" * 50)

def main():
    """主函数"""
    print_header()
    
    # 检查要求
    if not check_requirements():
        print("❌ 系统要求检查失败")
        return
    
    # 设置环境
    python_exe = setup_environment()
    
    # 创建配置文件
    create_env_file()
    
    # 显示配置指南
    show_config_guide()
    
    # 询问是否立即启动
    print("\n❓ 是否现在启动系统? (y/n): ", end="")
    choice = input().lower()
    
    if choice in ['y', 'yes', '是']:
        print("\n🚀 启动Astraeus系统...")
        subprocess.run([python_exe, "main.py"])
    else:
        print("\n✅ 设置完成！")
        print("请配置.env文件后运行: python main.py")

if __name__ == "__main__":
    main() 