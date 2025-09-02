# main.py
from loguru import logger

from src.config_manager import load_config
from src.data_loader import get_stock_data  # 导入函数
from src.indicator_MyTT import add_all_indicators
from src.utils import save_dataframe_to_processed

if __name__ == "__main__":
    cfg = load_config()
    logger.info("🚀 开始运行：获取数据并计算技术指标")

    df = get_stock_data()

    df = add_all_indicators(df)

    logger.info(df.tail(3))

    stock_code = df["股票代码"].iloc[0]
    save_dataframe_to_processed(df, f"{stock_code}", format=cfg["output_format"])
    logger.info("✅ 程序运行完毕。")
