import pandas as pd
from loguru import logger

from base import get_require_columns

# debug
from src.utils.get_data import get_stock_data
from src.utils.indicator_MyTT import add_all_indicators


class KdjSignal:
    def __init__(self):
        self.required_columns = ["kdj_k", "kdj_d", "kdj_j"]

    def get_kdj_columns(self, df: pd.DataFrame):
        df_kdj = get_require_columns(df, self.required_columns)
        logger.debug(df_kdj)
        return df_kdj


if __name__ == "__main__":
    debug_df = get_stock_data()
    debug_df = add_all_indicators(debug_df)
    kdj_signal = KdjSignal()
    kdj_signal.get_kdj_columns(debug_df)
