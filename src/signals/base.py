import pandas as pd


def get_latest_two_rows_for_crossover(
    df: pd.DataFrame, columns_of_interest: list
) -> pd.DataFrame:
    """
    从股票数据df中提取指定列的最新两行，用于金叉/死叉判断。

    参数:
        df (pd.DataFrame): 股票数据，索引为日期，包含技术指标列
        columns_of_interest (list): 感兴趣的列名列表，如 ['macd_dif', 'macd_dea', 'kdj_k', 'kdj_d']

    返回:
        pd.DataFrame: 最新两行数据，按时间倒序（最新在前）
    """
    # 提取指定列，并取最后两行（最新两个交易日）
    recent_data = df[columns_of_interest].tail(2)

    return recent_data
