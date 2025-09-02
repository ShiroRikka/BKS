# main.py
import pandas as pd
from loguru import logger

from src.utils.get_data import get_stock_data
from src.utils.indicator_MyTT import add_all_indicators

# 设置pandas显示选项，避免数据被截断
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
pd.set_option("display.max_colwidth", None)


def main():
    logger.info("🚀 开始运行：获取数据并计算技术指标")
    raw_df = get_stock_data()
    indicators_df = add_all_indicators(raw_df)


    logger.debug(indicators_df.tail(3))
    logger.info("✅ 程序运行完毕。")


if __name__ == "__main__":
    main()
