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
        提取 MACD 相关三列的最新两行数据
        """
        df_macd = get_require_columns(df, self.required_columns)
        logger.debug(df_macd)
        return df_macd

    def _is_golden_cross(self, df_macd: pd.DataFrame) -> bool:
        """
        判断是否发生金叉：DIF 由下向上穿越 DEA（昨日 DIF < DEA，今日 DIF > DEA）
        """
        prev, curr = df_macd.iloc[0], df_macd.iloc[1]
        golden = (prev["macd_dif"] < prev["macd_dea"]) and (
            curr["macd_dif"] > curr["macd_dea"]
        )
        if golden:
            logger.info("✅ 金叉形成：DIF 上穿 DEA")
        return golden

    def _is_dead_cross(self, df_macd: pd.DataFrame) -> bool:
        """
        判断是否发生死叉：DIF 由上向下穿越 DEA（昨日 DIF > DEA，今日 DIF < DEA）

        Args:
            df_macd (pd.DataFrame): 包含 macd_dif, macd_dea 的两行数据

        Returns:
            bool: 是否为死叉
        """
        prev, curr = df_macd.iloc[0], df_macd.iloc[1]
        dead = (prev["macd_dif"] > prev["macd_dea"]) and (
            curr["macd_dif"] < curr["macd_dea"]
        )
        if dead:
            logger.info("❌ 死叉形成：DIF 下穿 DEA")
        return dead

    def get_crossover_signal(self) -> str:
        """
        综合判断交叉信号类型

        Returns:
            str: 'golden_cross', 'dead_cross', 'no_cross'
        """
        df_macd = self.get_macd_columns()

        if self._is_golden_cross(df_macd):
            return "golden_cross"
        elif self._is_dead_cross(df_macd):
            return "dead_cross"
        else:
            return "no_cross"

    def get_zero_axis_position(self) -> str:
        """
        判断 DIF 当前处于零轴的哪个位置

        Returns:
            str: 'above'（上方）, 'below'（下方）, 'at_zero'（极近距离视为零轴）
        """
        df_macd = self.get_macd_columns()
        current_dif = df_macd.iloc[1]["macd_dif"]  # 最新一行 DIF 值

        tolerance = 1e-8  # 浮点误差容忍度
        if current_dif > tolerance:
            pos = "above"
        elif current_dif < -tolerance:
            pos = "below"
        else:
            pos = "at_zero"

        logger.debug("DIF 当前位置: %.4f -> %s 零轴", current_dif, pos)
        return pos


if __name__ == "__main__":
    debug_df = get_stock_data()
    debug_df = add_all_indicators(debug_df)
    macd_signal = MacdSignal()
    macd_signal.get_macd_columns(debug_df)
