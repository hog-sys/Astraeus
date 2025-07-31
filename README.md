# Astraeus - 加密货币智能交易与投资管理系统

![Astraeus Logo](https://img.shields.io/badge/Astraeus-Crypto%20Trading%20System-blue)
![Python](https://img.shields.io/badge/Python-3.8+-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 🌟 系统概述

Astraeus 是一个尖端、自主的智能交易与投资管理系统，专为加密货币市场设计。系统以**最大化风险调整后收益**为核心使命，同时严格遵守预设的风险管理框架和投资纪律。

### 🎯 核心特性

- **🤖 自主智能**: 完全自动化的交易决策和执行
- **📊 多维分析**: 技术分析、基本面分析、情绪分析的综合评估
- **🛡️ 风险管理**: 基于凯利准则的动态头寸计算和投资组合风险控制
- **⚡ 实时监控**: 24/7 实时持仓监控和止损止盈管理
- **📱 远程控制**: Telegram 指挥中心，随时随地掌控系统
- **📈 绩效分析**: 详细的交易记录和绩效归因分析

## 🏗️ 系统架构

### 七大核心模块

1. **系统配置与初始化** - 安全环境加载和策略参数化
2. **数据层聚合与处理** - 多源数据管道和智能缓存
3. **分析与决策引擎** - 多维分析框架和自适应加权评分
4. **风险管理与头寸控制** - 动态头寸计算和投资组合风险评估
5. **交易执行与监控** - 智能订单路由和原子化交易执行
6. **投资组合管理与优化** - 绩效归因分析和自动再平衡
7. **自动化调度与报告** - 异步任务调度和定时报告生成

## 🚀 快速开始

### 环境要求

- Python 3.8+
- SQLite 3.x (或 PostgreSQL)
- 稳定的网络连接

### 安装步骤

1. **克隆项目**
```bash
git clone https://github.com/your-username/astraeus.git
cd astraeus
```

2. **创建虚拟环境**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate  # Windows
```

3. **安装依赖**
```bash
pip install -r requirements.txt
```

4. **配置环境变量**
```bash
cp env_example.txt .env
# 编辑 .env 文件，填入您的API密钥和配置
```

5. **运行系统**
```bash
python main.py
```

## ⚙️ 配置说明

### 必需配置

#### 交易所API (Binance)
```env
BINANCE_API_KEY=your_binance_api_key_here
BINANCE_SECRET_KEY=your_binance_secret_key_here
BINANCE_TESTNET=false  # 建议先使用测试网
```

#### Telegram Bot
```env
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
TELEGRAM_CHAT_ID=your_telegram_chat_id_here
```

### 可选配置

#### 数据源API
```env
POLYGON_API_KEY=your_polygon_api_key_here
ALPHA_VANTAGE_API_KEY=your_alpha_vantage_api_key_here
GLASSNODE_API_KEY=your_glassnode_api_key_here
```

#### 交易参数
```env
MAX_DAILY_DEPLOYMENT_USDC=1000  # 单日最大部署资金
MAX_CONCURRENT_POSITIONS=5       # 最大并发持仓数量
DEFAULT_STOP_LOSS_PERCENT=2.0    # 默认止损百分比
DEFAULT_TAKE_PROFIT_PERCENT=6.0  # 默认止盈百分比
```

## 📱 Telegram 命令

系统支持通过 Telegram 进行远程控制：

- `/status` - 查看系统状态和持仓
- `/pause` - 暂停交易
- `/resume` - 恢复交易
- `/panic` - 紧急平仓所有持仓
- `/help` - 显示帮助信息

## 📊 系统功能

### 智能分析
- **技术分析**: RSI、MACD、布林带、移动平均线等
- **基本面分析**: 市值、流动性、社区活跃度评估
- **情绪分析**: 社交媒体和链上数据情绪分析

### 风险管理
- **动态头寸计算**: 基于凯利准则和信号强度
- **投资组合VaR**: 实时风险价值计算
- **黑天鹅应对**: 极端市场条件下的自动风险控制

### 交易执行
- **智能订单路由**: 自动选择最优交易所
- **原子化执行**: 确保交易和数据库的一致性
- **实时监控**: 24/7 持仓监控和止损止盈

## 🔧 开发指南

### 项目结构
```
astraeus/
├── src/
│   ├── config/          # 配置管理
│   ├── database/        # 数据库模型和管理
│   ├── data/           # 数据聚合和处理
│   ├── analysis/       # 分析引擎
│   ├── risk/           # 风险管理
│   ├── trading/        # 交易执行
│   ├── notifications/  # 通知服务
│   └── scheduler/      # 任务调度
├── logs/               # 日志文件
├── main.py            # 主程序入口
├── requirements.txt   # 依赖包
└── README.md         # 项目文档
```

### 添加新功能

1. **创建新模块**: 在 `src/` 目录下创建新的模块
2. **更新配置**: 在 `src/config/settings.py` 中添加新配置
3. **集成调度**: 在 `src/scheduler/automation.py` 中添加新任务
4. **测试验证**: 编写测试用例确保功能正确性

## 📈 性能监控

### 关键指标
- **交易成功率**: 订单执行成功率
- **风险调整收益**: 夏普比率、最大回撤
- **系统稳定性**: 运行时间、错误率
- **API调用效率**: 请求成功率、响应时间

### 日志分析
系统日志存储在 `logs/astraeus.log`，包含：
- 交易执行记录
- 错误和异常信息
- 系统性能指标
- 风险监控数据

## ⚠️ 风险提示

### 重要声明
- 本系统仅供学习和研究使用
- 加密货币交易存在高风险，可能导致资金损失
- 请在使用前充分了解相关风险
- 建议先在测试环境中验证系统功能

### 安全建议
- 定期备份数据库
- 使用强密码和双因素认证
- 监控API密钥使用情况
- 定期检查系统日志

## 🤝 贡献指南

欢迎贡献代码和提出建议！

1. Fork 项目
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开 Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 📞 联系方式

- 项目主页: [GitHub Repository](https://github.com/hog-sys/astraeus)
- 问题反馈: [Issues](https://github.com/hog-sys/astraeus/issues)
- 功能建议: [Discussions](https://github.com/hog-sys/astraeus/discussions)

**免责声明**: 本软件仅供教育和研究目的。使用本软件进行实际交易的风险由用户自行承担。开发者不对任何投资损失承担责任。 
