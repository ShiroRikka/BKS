import pandas as pd
from loguru import logger

from base import get_require_columns

# debug
from src.utils.get_data import get_stock_data
from src.utils.indicator_MyTT import add_all_indicators


class MacdSignal:
    def __init__(self):
        self.required_columns = ["macd_dif", "macd_dea", "macd"]

    def get_macd_columns(self, df: pd.DataFrame):
        """
        提取 MACD 相关三列数据
        """
        df_macd = get_require_columns(df, self.required_columns)
        # logger.debug(df_macd)
        return df_macd

    def _is_golden_cross(self, df_macd: pd.DataFrame) -> bool:
        """
        判断是否发生金叉：DIF 由下向上穿越 DEA（昨日 DIF < DEA，今日 DIF > DEA）
        """
        today, yesterday = df_macd.iloc[-1], df_macd.iloc[-2]
        # logger.debug(f"today:{today};yesterday:{yesterday}")
        golden = (yesterday["macd_dif"] < yesterday["macd_dea"]) and (
            today["macd_dif"] > today["macd_dea"]
        )
        if golden:
            logger.info("✅ 金叉形成：DIF 上穿 DEA")
        return golden

    def _is_dead_cross(self, df_macd: pd.DataFrame) -> bool:
        """
        判断是否发生死叉：DIF 由上向下穿越 DEA（昨日 DIF > DEA，今日 DIF < DEA）
        """
        today, yesterday = df_macd.iloc[-1], df_macd.iloc[-2]
        dead = (yesterday["macd_dif"] > yesterday["macd_dea"]) and (
            today["macd_dif"] < today["macd_dea"]
        )
        if dead:
            logger.info("❌ 死叉形成：DIF 下穿 DEA")
        return dead

    def get_crossover_signal(self,df: pd.DataFrame) -> int:
        """
        综合判断交叉信号类型
        :param df: pd.DataFrame

        """
        df_macd = self.get_macd_columns(df)

        if self._is_golden_cross(df_macd):
            return 1
        elif self._is_dead_cross(df_macd):
            return -1
        else:
            return 0

if __name__ == "__main__":
    debug_df = get_stock_data()
    debug_df = add_all_indicators(debug_df)
    macd_signal = MacdSignal()
    logger.debug(macd_signal.get_crossover_signal(debug_df))
