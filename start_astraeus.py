#!/usr/bin/env python3
"""
Astraeus 简化启动脚本
确保使用正确的虚拟环境
"""

import sys
import os
import subprocess
from pathlib import Path

def check_environment():
    """检查环境"""
    print("🔍 检查运行环境...")
    
    # 检查是否在虚拟环境中
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("✅ 正在使用虚拟环境")
    else:
        print("⚠️  未检测到虚拟环境，尝试使用项目虚拟环境")
        return False
    
    # 检查Python版本
    print(f"Python版本: {sys.version}")
    
    # 检查关键模块
    try:
        import loguru
        print("✅ loguru 模块可用")
    except ImportError:
        print("❌ loguru 模块不可用")
        return False
    
    try:
        import ta
        print("✅ ta 模块可用")
    except ImportError:
        print("❌ ta 模块不可用")
        return False
    
    try:
        import pandas
        print("✅ pandas 模块可用")
    except ImportError:
        print("❌ pandas 模块不可用")
        return False
    
    return True

def start_with_venv():
    """使用虚拟环境启动"""
    print("\n🚀 使用虚拟环境启动Astraeus...")
    
    # 确定虚拟环境Python路径
    if os.name == 'nt':  # Windows
        python_exe = "venv\\Scripts\\python.exe"
    else:  # Unix/Linux/macOS
        python_exe = "venv/bin/python"
    
    # 检查虚拟环境是否存在
    if not Path(python_exe).exists():
        print(f"❌ 虚拟环境不存在: {python_exe}")
        return False
    
    try:
        # 启动主程序
        result = subprocess.run([python_exe, "main.py"], 
                              capture_output=False, 
                              text=True)
        return result.returncode == 0
    except Exception as e:
        print(f"❌ 启动失败: {e}")
        return False

def show_help():
    """显示帮助信息"""
    print("\n" + "=" * 60)
    print("🔧 Astraeus 启动帮助")
    print("=" * 60)
    print()
    print("如果遇到模块导入错误，请尝试以下步骤：")
    print()
    print("1. 激活虚拟环境:")
    print("   # Windows:")
    print("   venv\\Scripts\\activate")
    print("   # macOS/Linux:")
    print("   source venv/bin/activate")
    print()
    print("2. 安装缺失的依赖:")
    print("   pip install ta pandas numpy loguru")
    print()
    print("3. 检查配置:")
    print("   - 确保 .env 文件存在")
    print("   - 检查API密钥配置")
    print()
    print("4. 手动启动:")
    print("   python main.py")
    print()
    print("5. 查看日志:")
    print("   # Windows:")
    print("   type astraeus.log")
    print("   # macOS/Linux:")
    print("   tail -f astraeus.log")
    print("=" * 60)

def main():
    """主函数"""
    print("🚀 Astraeus 智能交易系统启动器")
    print("=" * 50)
    
    # 检查环境
    if not check_environment():
        print("\n❌ 环境检查失败")
        show_help()
        return
    
    # 尝试启动
    if not start_with_venv():
        print("\n❌ 启动失败")
        show_help()
        return
    
    print("\n✅ Astraeus 启动完成")

if __name__ == "__main__":
    main() 