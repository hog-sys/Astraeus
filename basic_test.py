"""
Astraeus 基础测试
测试项目结构和文件完整性
"""

import sys
import os
from pathlib import Path

def test_project_structure():
    """测试项目结构"""
    print("🔍 测试项目结构...")
    
    required_files = [
        "main.py",
        "requirements.txt", 
        "env_example.txt",
        "README.md",
        "src/__init__.py",
        "src/config/__init__.py",
        "src/config/settings.py",
        "src/database/__init__.py",
        "src/database/models.py",
        "src/database/manager.py",
        "src/data/__init__.py",
        "src/data/providers.py",
        "src/analysis/__init__.py",
        "src/analysis/engine.py",
        "src/risk/__init__.py",
        "src/risk/manager.py",
        "src/trading/__init__.py",
        "src/trading/executor.py",
        "src/notifications/__init__.py",
        "src/notifications/telegram.py",
        "src/scheduler/__init__.py",
        "src/scheduler/automation.py"
    ]
    
    missing_files = []
    for file_path in required_files:
        if not os.path.exists(file_path):
            missing_files.append(file_path)
    
    if missing_files:
        print(f"❌ 缺少文件: {missing_files}")
        return False
    else:
        print("✅ 项目结构完整")
        return True

def test_file_sizes():
    """测试文件大小"""
    print("📏 测试文件大小...")
    
    python_files = []
    for root, dirs, files in os.walk("src"):
        for file in files:
            if file.endswith(".py"):
                python_files.append(os.path.join(root, file))
    
    python_files.append("main.py")
    
    empty_files = []
    for file_path in python_files:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read().strip()
                if not content:
                    empty_files.append(file_path)
        except Exception as e:
            print(f"⚠️ 无法读取文件 {file_path}: {e}")
    
    if empty_files:
        print(f"⚠️ 空文件: {empty_files}")
        return False
    else:
        print(f"✅ 所有 {len(python_files)} 个Python文件都有内容")
        return True

def test_import_structure():
    """测试导入结构"""
    print("📦 测试导入结构...")
    
    # 检查__init__.py文件
    init_files = [
        "src/__init__.py",
        "src/config/__init__.py",
        "src/database/__init__.py",
        "src/data/__init__.py",
        "src/analysis/__init__.py",
        "src/risk/__init__.py",
        "src/trading/__init__.py",
        "src/notifications/__init__.py",
        "src/scheduler/__init__.py"
    ]
    
    missing_inits = []
    for init_file in init_files:
        if not os.path.exists(init_file):
            missing_inits.append(init_file)
    
    if missing_inits:
        print(f"❌ 缺少__init__.py文件: {missing_inits}")
        return False
    else:
        print("✅ 所有包都有__init__.py文件")
        return True

def test_config_content():
    """测试配置文件内容"""
    print("⚙️ 测试配置文件内容...")
    
    config_files = [
        "requirements.txt",
        "env_example.txt",
        "README.md"
    ]
    
    for config_file in config_files:
        if not os.path.exists(config_file):
            print(f"❌ 配置文件不存在: {config_file}")
            return False
        
        try:
            with open(config_file, "r", encoding="utf-8") as f:
                content = f.read()
                if len(content.strip()) < 10:  # 至少10个字符
                    print(f"⚠️ 配置文件内容过少: {config_file}")
                    return False
        except Exception as e:
            print(f"❌ 无法读取配置文件 {config_file}: {e}")
            return False
    
    print("✅ 所有配置文件都有内容")
    return True

def test_python_syntax():
    """测试Python语法"""
    print("🐍 测试Python语法...")
    
    python_files = []
    for root, dirs, files in os.walk("src"):
        for file in files:
            if file.endswith(".py"):
                python_files.append(os.path.join(root, file))
    
    python_files.append("main.py")
    
    syntax_errors = []
    for file_path in python_files:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                compile(f.read(), file_path, "exec")
        except SyntaxError as e:
            syntax_errors.append(f"{file_path}: {e}")
        except Exception as e:
            syntax_errors.append(f"{file_path}: {e}")
    
    if syntax_errors:
        print(f"❌ 语法错误: {syntax_errors}")
        return False
    else:
        print(f"✅ 所有 {len(python_files)} 个Python文件语法正确")
        return True

def test_directory_structure():
    """测试目录结构"""
    print("📁 测试目录结构...")
    
    required_dirs = [
        "src",
        "src/config",
        "src/database", 
        "src/data",
        "src/analysis",
        "src/risk",
        "src/trading",
        "src/notifications",
        "src/scheduler"
    ]
    
    missing_dirs = []
    for dir_path in required_dirs:
        if not os.path.exists(dir_path):
            missing_dirs.append(dir_path)
    
    if missing_dirs:
        print(f"❌ 缺少目录: {missing_dirs}")
        return False
    else:
        print("✅ 目录结构完整")
        return True

def run_all_tests():
    """运行所有基础测试"""
    print("🚀 开始 Astraeus 基础测试...\n")
    
    tests = [
        ("项目结构", test_project_structure),
        ("文件大小", test_file_sizes),
        ("导入结构", test_import_structure),
        ("配置文件", test_config_content),
        ("Python语法", test_python_syntax),
        ("目录结构", test_directory_structure)
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
        print("🎉 所有基础测试通过！")
        print("\n📋 Astraeus系统状态:")
        print("✅ 项目结构完整")
        print("✅ 所有文件存在且有内容")
        print("✅ Python语法正确")
        print("✅ 包结构正确")
        print("✅ 配置文件完整")
        print("\n💡 下一步操作:")
        print("1. 安装依赖: pip install -r requirements.txt")
        print("2. 配置环境变量: 复制 env_example.txt 为 .env")
        print("3. 启动系统: python main.py")
        print("\n🌟 Astraeus系统已准备就绪！")
    else:
        print("⚠️ 部分测试失败，请检查项目结构。")
    
    return passed == total

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1) 