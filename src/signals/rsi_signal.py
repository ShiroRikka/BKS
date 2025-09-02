import pandas as pd
from loguru import logger

from base import get_require_columns

# debug
from src.utils.get_data import get_stock_data
from src.utils.indicator_MyTT import add_all_indicators


class RsiSignal:
    def __init__(self):
        self.required_colums = ["rsi_14"]

    def get_rsi_columns(self, df: pd.DataFrame):
        df_rsi = get_require_columns(df, self.required_colums)
        logger.debug(df_rsi)
        return df_rsi


if __name__ == "__main__":
    debug_df = get_stock_data()
    debug_df = add_all_indicators(debug_df)
    rsi_signal = RsiSignal()
    rsi_signal.get_rsi_columns(debug_df)
