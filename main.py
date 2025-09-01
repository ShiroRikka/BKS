# main.py
from loguru import logger

from src.data_loader import get_stock_data  # 导入函数

if __name__ == "__main__":
    df = get_stock_data()
    logger.info(df.tail(3))
