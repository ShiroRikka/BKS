# main.py
from loguru import logger

from src.utils.get_data import get_stock_data
from src.utils.indicator_MyTT import add_all_indicators

if __name__ == "__main__":
    logger.info("🚀 开始运行：获取数据并计算技术指标")

    raw_df = get_stock_data()

    indicators_df = add_all_indicators(raw_df)

    result_df = indicators_df

    logger.debug(result_df.tail(3))
    logger.info("✅ 程序运行完毕。")
