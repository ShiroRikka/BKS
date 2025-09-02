# main.py
from loguru import logger


from src.utils.get_data import get_stock_data  # 导入函数

if __name__ == "__main__":
    logger.info("🚀 开始运行：获取数据并计算技术指标")

    df = get_stock_data()

    # df = add_all_indicators(df)

    logger.info(df.tail(3))

    # stock_code = df["股票代码"].iloc[0]
    logger.info("✅ 程序运行完毕。")
