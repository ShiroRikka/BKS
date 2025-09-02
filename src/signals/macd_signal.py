import pandas as pd
from loguru import logger

from base import get_latest_two_rows_for_crossover

# debug
from src.utils.get_data import get_stock_data
from src.utils.indicator_MyTT import add_all_indicators


class MacdSignal:
    def __init__(self):
        self.required_columns = ["macd_dif", "macd_dea", "macd"]

    def get_macd_columns(self, df: pd.DataFrame):
        df_macd = get_latest_two_rows_for_crossover(df, self.required_columns)
        logger.debug(df_macd)
        return df_macd


if __name__ == "__main__":
    debug_df = get_stock_data()
    debug_df = add_all_indicators(debug_df)
    macd_signal = MacdSignal()
    macd_signal.get_macd_columns(debug_df)
