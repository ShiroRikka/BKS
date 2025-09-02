import pandas as pd


def get_require_columns(df: pd.DataFrame, require_columns: list) -> pd.DataFrame:
    """
    从股票数据 DataFrame 中提取指定列，以支持各类指标的计算与分析。
    :param df: pd.DataFrame，包含预先计算好的技术指标数据。
    :param require_columns: 所需提取的列名列表，例如 ['macd_dif', 'macd_dea', 'kdj_k', 'kdj_d']。
    :return: pd.DataFrame，包含所选列的股票数据。
    """
    require_columns = df[require_columns]
    return require_columns
