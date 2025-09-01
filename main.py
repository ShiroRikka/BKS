# main.py
from src.data_loader import get_stock_data  # 导入函数

if __name__ == "__main__":
    df = get_stock_data()
    print(df.tail(3))


