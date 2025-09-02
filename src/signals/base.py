import pandas as pd


def get_require_columns(df: pd.DataFrame, require_columns: list) -> pd.DataFrame:
    """
    从股票数据df中提取指定列，为不同指标提供数据支持。

    参数:
        df (pd.DataFrame): 股票数据，索引为日期，包含技术指标列
        require_columns (list): 需要的列名列表，如 ['macd_dif', 'macd_dea', 'kdj_k', 'kdj_d']

    返回:
        pd.DataFrame: 需要的列（最新的数据在最下面）
    """
    require_columns = df[require_columns]
    return require_columns
