# Astraeus 智能交易系统部署指南

## 🚀 系统概述

Astraeus 是一个为加密货币市场设计的尖端、自主的智能交易与投资管理系统。系统具备数据洞察、决策智能和自我进化能力，能够最大化风险调整后收益，同时严格遵守预设的风险管理框架。

### 核心特性
- 🔄 **多源数据聚合** - Binance、CoinGecko、Polygon等
- 📈 **多维分析引擎** - 技术、基本面、情绪分析
- 🛡️ **智能风险管理** - 动态止损止盈、VaR控制
- 🤖 **自动化交易** - 智能订单执行和监控
- 📱 **Telegram控制** - 实时通知和远程控制
- 📊 **性能分析** - 投资组合优化和回测

## 📋 系统要求

### 硬件要求
- **CPU**: 2核心以上
- **内存**: 4GB RAM以上
- **存储**: 10GB可用空间
- **网络**: 稳定的互联网连接

### 软件要求
- **操作系统**: Windows 10/11, macOS, Linux
- **Python**: 3.8+ (推荐3.9+)
- **数据库**: SQLite (内置，无需额外安装)

## 🛠️ 快速部署

### 1. 环境准备

```bash
# 克隆项目
git clone <repository-url>
cd Astraeus

# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 2. 安装依赖

```bash
# 安装所有依赖包
pip install -r requirements.txt
```

### 3. 配置环境变量

复制环境变量模板并配置您的API密钥：

```bash
# Windows
copy env_example.txt .env

# macOS/Linux
cp env_example.txt .env
```

编辑 `.env` 文件，配置以下必要参数：

```env
# Binance API配置 (必需)
BINANCE_API_KEY=your_binance_api_key
BINANCE_SECRET_KEY=your_binance_secret_key
BINANCE_TESTNET=true

# Telegram配置 (必需)
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=your_telegram_chat_id

# 可选API配置
CUCOIN_API=your_cucoin_api_key
COINGECKO_API_KEY=your_coingecko_api_key
POLYGON_API_KEY=your_polygon_api_key
ALPHA_VANTAGE_API_KEY=your_alpha_vantage_api_key
GLASSNODE_API_KEY=your_glassnode_api_key

# 系统配置
DATABASE_URL=sqlite:///trading_system.db
LOG_LEVEL=INFO

# 交易参数
MAX_DAILY_DEPLOYMENT_USDC=10
MAX_CONCURRENT_POSITIONS=3
DEFAULT_STOP_LOSS_PERCENT=2.0
DEFAULT_TAKE_PROFIT_PERCENT=6.0
RISK_PER_TRADE_PERCENT=1.0

# 分析权重
TECHNICAL_ANALYSIS_WEIGHT=0.4
FUNDAMENTAL_ANALYSIS_WEIGHT=0.4
SENTIMENT_ANALYSIS_WEIGHT=0.2

# 调度配置
DATA_UPDATE_INTERVAL_MINUTES=5
ANALYSIS_INTERVAL_MINUTES=10
PORTFOLIO_REBALANCE_INTERVAL_HOURS=24

# 风险控制
MAX_PORTFOLIO_VAR_PERCENT=5.0
```

### 4. 启动系统

```bash
# 启动主系统
python main.py
```

#### 便捷启动方式

**Windows用户:**
```bash
launch.bat
```

**Linux/macOS用户:**
```bash
./launch.sh
```

#### 系统验证

启动前可以运行以下命令验证系统：

```bash
# 快速测试
python test_quick.py

# 状态检查
python status.py
```

## 🔑 API密钥获取指南

### Binance API
1. 访问 [Binance官网](https://www.binance.com)
2. 登录账户 → API管理
3. 创建新的API密钥
4. 启用现货交易权限
5. 设置IP白名单（推荐）

### Telegram Bot
1. 在Telegram中搜索 `@BotFather`
2. 发送 `/newbot` 命令
3. 按提示设置机器人名称
4. 获取Bot Token
5. 将机器人添加到群组或频道
6. 获取Chat ID（使用 `@userinfobot`）

### 可选API密钥
- **CoinGecko**: 免费API，无需密钥（有速率限制）
- **Polygon**: 注册获取免费API密钥
- **Alpha Vantage**: 注册获取免费API密钥
- **Glassnode**: 注册获取API密钥

## 📱 Telegram命令

系统启动后，您可以通过Telegram与系统交互：

| 命令 | 功能 | 示例 |
|------|------|------|
| `/status` | 获取系统状态和持仓信息 | `/status` |
| `/pause` | 暂停开新仓位 | `/pause` |
| `/resume` | 恢复交易 | `/resume` |
| `/panic` | 紧急清仓所有持仓 | `/panic` |
| `/help` | 显示帮助信息 | `/help` |

## 🔧 系统配置

### 交易参数调整

在 `.env` 文件中可以调整以下参数：

```env
# 资金管理
MAX_DAILY_DEPLOYMENT_USDC=10          # 单日最大部署资金
MAX_CONCURRENT_POSITIONS=3             # 最大并发持仓数

# 风险控制
DEFAULT_STOP_LOSS_PERCENT=2.0          # 默认止损百分比
DEFAULT_TAKE_PROFIT_PERCENT=6.0        # 默认止盈百分比
RISK_PER_TRADE_PERCENT=1.0             # 每笔交易风险百分比
MAX_PORTFOLIO_VAR_PERCENT=5.0          # 最大投资组合VaR

# 分析权重
TECHNICAL_ANALYSIS_WEIGHT=0.4          # 技术分析权重
FUNDAMENTAL_ANALYSIS_WEIGHT=0.4        # 基本面分析权重
SENTIMENT_ANALYSIS_WEIGHT=0.2          # 情绪分析权重
```

### 调度配置

```env
# 数据更新频率
DATA_UPDATE_INTERVAL_MINUTES=5         # 数据更新间隔
ANALYSIS_INTERVAL_MINUTES=10           # 分析间隔
PORTFOLIO_REBALANCE_INTERVAL_HOURS=24  # 再平衡间隔
```

## 📊 系统监控

### 日志文件
- **主日志**: `astraeus.log`
- **错误日志**: `error.log`
- **交易日志**: `trades.log`

### 数据库文件
- **主数据库**: `trading_system.db`
- **备份目录**: `backups/`

### 实时监控
```bash
# 查看实时日志
tail -f astraeus.log

# 查看系统状态
python -c "from src.config.settings import config; print(config.get_config_dict())"
```

## 🚨 故障排除

### 常见问题

#### 1. 依赖安装失败
```bash
# 升级pip
python -m pip install --upgrade pip

# 使用国内镜像
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/
```

#### 2. API密钥错误
- 检查API密钥是否正确配置
- 确认API权限设置
- 验证IP白名单设置

#### 3. 数据库连接错误
```bash
# 重新初始化数据库
python -c "from src.database.manager import db_manager; db_manager.initialize()"
```

#### 4. Telegram通知失败
- 检查Bot Token是否正确
- 确认Chat ID是否正确
- 验证机器人是否已添加到群组

### 调试模式

启用详细日志：
```env
LOG_LEVEL=DEBUG
```

## 🔒 安全建议

### API密钥安全
1. **永远不要**将API密钥提交到代码仓库
2. 使用环境变量存储敏感信息
3. 定期轮换API密钥
4. 设置IP白名单限制访问

### 系统安全
1. 使用强密码保护系统
2. 定期备份数据库
3. 监控异常交易活动
4. 设置合理的风险限制

### 资金安全
1. 从小额开始测试
2. 设置严格的止损
3. 定期检查持仓
4. 监控系统性能

## 📈 性能优化

### 系统优化
- 调整缓存时间减少API调用
- 优化数据库查询
- 使用SSD存储提升I/O性能

### 网络优化
- 使用稳定的网络连接
- 配置合适的超时时间
- 实现重试机制

## 🔄 更新和维护

### 系统更新
```bash
# 拉取最新代码
git pull origin main

# 更新依赖
pip install -r requirements.txt --upgrade

# 重启系统
python main.py
```

### 数据备份
```bash
# 备份数据库
python -c "from src.database.manager import db_manager; db_manager.backup_database()"

# 清理旧数据
python -c "from src.database.manager import db_manager; db_manager.cleanup_old_data()"
```

## ⚠️ 风险警告

### 重要声明
1. **加密货币交易存在高风险**，可能导致资金损失
2. **本系统仅供学习和研究使用**
3. **请根据自身风险承受能力谨慎使用**
4. **建议先在测试环境中充分验证**

### 免责声明
- 开发者不对任何交易损失承担责任
- 用户应自行承担交易风险
- 建议咨询专业投资顾问

## 📞 技术支持

### 获取帮助
- 查看日志文件获取错误信息
- 检查配置文件是否正确
- 验证网络连接和API状态

### 社区支持
- GitHub Issues: 报告问题和功能请求
- 文档: 查看详细技术文档
- 讨论: 加入用户社区

---

**版本**: 1.0.0  
**最后更新**: 2025-07-31  
**维护者**: Astraeus Team 