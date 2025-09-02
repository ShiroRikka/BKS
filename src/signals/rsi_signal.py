import pandas as pd
from loguru import logger

from base import get_latest_two_rows_for_crossover

# debug
from src.utils.get_data import get_stock_data
from src.utils.indicator_MyTT import add_all_indicators


def get_rsi_columns(df: pd.DataFrame):
    df_rsi = get_latest_two_rows_for_crossover(df, ["rsi_14"])
    logger.debug(df_rsi)
    return df_rsi


if __name__ == "__main__":
    debug_df = get_stock_data()
    debug_df = add_all_indicators(debug_df)
    get_rsi_columns(debug_df)
