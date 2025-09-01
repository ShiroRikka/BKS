# main.py
from loguru import logger

from src.data_loader import get_stock_data  # 导入函数
from src.indicator import add_all_indicators
from src.utils import save_dataframe_to_processed





if __name__ == "__main__":
    logger.info("🚀 开始运行：获取数据并计算技术指标")

    df = get_stock_data()


    logger.info("🧾 各列数据类型如下：")
    for col in df.columns:
        dtype = df[col].dtype
        sample = df[col].iloc[1]
        logger.info(f"  📌 {col}: {dtype}，示例值 = {sample}")



    df = add_all_indicators(df)

    logger.info(df.tail(3))

    stock_code = df['股票代码'].iloc[0]
    # save_dataframe_to_processed(df, f"{stock_code}", format="parquet")
    save_dataframe_to_processed(df, f"{stock_code}", format="csv")
    logger.info("✅ 程序运行完毕。")