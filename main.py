"""
Astraeus - 加密货币智能交易与投资管理系统
主程序入口
"""

import asyncio
import signal
import sys
from loguru import logger
from pathlib import Path

# 添加src目录到Python路径
sys.path.append(str(Path(__file__).parent / "src"))

from src.config.settings import config
from src.database.manager import db_manager
from src.scheduler.automation import automation_scheduler
from src.notifications.telegram import telegram_notifier


class AstraeusSystem:
    """Astraeus 主系统"""
    
    def __init__(self):
        self.running = False
        self.setup_logging()
        self.setup_signal_handlers()
    
    def setup_logging(self):
        """设置日志"""
        logger.remove()  # 移除默认处理器
        
        # 添加控制台处理器
        logger.add(
            sys.stdout,
            format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
            level=config.system.log_level,
            colorize=True
        )
        
        # 添加文件处理器
        logger.add(
            "logs/astraeus.log",
            rotation="1 day",
            retention="30 days",
            format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
            level="DEBUG"
        )
        
        logger.info("Astraeus 系统启动中...")
    
    def setup_signal_handlers(self):
        """设置信号处理器"""
        def signal_handler(signum, frame):
            logger.info(f"收到信号 {signum}，正在优雅关闭...")
            self.running = False
        
        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)
    
    async def initialize(self):
        """初始化系统"""
        try:
            logger.info("正在初始化 Astraeus 系统...")
            
            # 初始化数据库
            db_manager.initialize()
            logger.info("数据库初始化完成")
            
            # 测试数据库连接
            if not db_manager.test_connection():
                raise Exception("数据库连接测试失败")
            
            # 初始化资产数据（如果需要）
            await self._initialize_assets()
            
            logger.info("系统初始化完成")
            
        except Exception as e:
            logger.error(f"系统初始化失败: {e}")
            raise
    
    async def _initialize_assets(self):
        """初始化资产数据"""
        try:
            from src.database.models import Asset
            from src.data.providers import data_aggregator
            
            async with db_manager.get_session_async() as session:
                # 检查是否已有资产数据
                existing_assets = session.query(Asset).count()
                
                if existing_assets == 0:
                    logger.info("正在初始化资产数据...")
                    
                    # 获取市值排名前20的资产
                    top_assets = await data_aggregator.get_top_market_cap_assets(limit=20)
                    
                    for asset_data in top_assets:
                        asset = Asset(
                            symbol=asset_data["symbol"],
                            name=asset_data["name"],
                            asset_type="CRYPTO",  # 简化处理
                            market_cap=asset_data["market_cap"],
                            volume_24h=asset_data["volume_24h"],
                            price=asset_data["price"],
                            price_change_24h=asset_data["price_change_24h"],
                            is_active=True,
                            exchange_support="binance"
                        )
                        session.add(asset)
                    
                    session.commit()
                    logger.info(f"已初始化 {len(top_assets)} 个资产")
                else:
                    logger.info(f"已有 {existing_assets} 个资产，跳过初始化")
                    
        except Exception as e:
            logger.error(f"初始化资产数据失败: {e}")
    
    async def start(self):
        """启动系统"""
        try:
            await self.initialize()
            
            # 启动自动化调度器
            await automation_scheduler.start()
            
            self.running = True
            logger.info("🚀 Astraeus 系统启动成功！")
            
            # 发送启动通知
            await telegram_notifier.send_notification("🚀 Astraeus 系统已启动并开始运行")
            
            # 主循环
            while self.running:
                await asyncio.sleep(1)
            
        except Exception as e:
            logger.error(f"系统启动失败: {e}")
            await telegram_notifier.send_error_notification(str(e), "System")
            raise
    
    async def shutdown(self):
        """关闭系统"""
        try:
            logger.info("正在关闭 Astraeus 系统...")
            
            # 停止调度器
            await automation_scheduler.stop()
            
            # 关闭数据库连接
            db_manager.close()
            
            # 发送关闭通知
            await telegram_notifier.send_notification("🛑 Astraeus 系统已关闭")
            
            logger.info("Astraeus 系统已安全关闭")
            
        except Exception as e:
            logger.error(f"系统关闭失败: {e}")


async def main():
    """主函数"""
    system = AstraeusSystem()
    
    try:
        await system.start()
    except KeyboardInterrupt:
        logger.info("收到中断信号")
    except Exception as e:
        logger.error(f"系统运行错误: {e}")
    finally:
        await system.shutdown()


if __name__ == "__main__":
    # 创建日志目录
    Path("logs").mkdir(exist_ok=True)
    
    # 运行主程序
    asyncio.run(main()) 