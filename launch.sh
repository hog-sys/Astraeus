#!/bin/bash

echo "========================================"
echo "   Astraeus 智能交易系统启动器"
echo "========================================"
echo

# 检查虚拟环境是否存在
if [ ! -f "venv/bin/activate" ]; then
    echo "❌ 虚拟环境不存在，请先运行以下命令："
    echo "python3 -m venv venv"
    echo "source venv/bin/activate"
    echo "pip install -r requirements.txt"
    exit 1
fi

# 激活虚拟环境
echo "🔧 激活虚拟环境..."
source venv/bin/activate

# 检查.env文件是否存在
if [ ! -f ".env" ]; then
    echo "⚠️  配置文件不存在，正在创建..."
    if [ -f "env_example.txt" ]; then
        cp env_example.txt .env
        echo "✅ 配置文件已创建，请编辑 .env 文件配置您的API密钥"
        echo
        echo "按任意键打开配置文件..."
        read -n 1
        if command -v nano &> /dev/null; then
            nano .env
        elif command -v vim &> /dev/null; then
            vim .env
        else
            echo "请手动编辑 .env 文件"
        fi
    else
        echo "❌ env_example.txt 文件不存在"
        exit 1
    fi
fi

# 检查依赖是否安装
echo "🔍 检查依赖..."
python -c "import asyncio, aiohttp, pandas, numpy, loguru, pydantic_settings" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "❌ 依赖未完全安装，正在安装..."
    pip install -r requirements.txt
    if [ $? -ne 0 ]; then
        echo "❌ 依赖安装失败"
        exit 1
    fi
fi

# 启动系统
echo
echo "🚀 启动 Astraeus 系统..."
echo
python main.py

# 如果系统异常退出，显示错误信息
if [ $? -ne 0 ]; then
    echo
    echo "❌ 系统启动失败，请检查配置和日志"
    read -n 1
fi 