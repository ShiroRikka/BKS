# src/indicator.py
import pandas as pd
import talib as ta
from loguru import logger


def add_trend_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """添加趋势类指标"""
    df = df.copy()

    # MACD
    df["DIF"], df["MACE_DEA"], df["MACD_M"] = ta.MACD(
        df["close"].values, fastperiod=12, slowperiod=26, signalperiod=9
    )

    logger.info("📈 趋势类指标计算完成：MACD")
    return df


def add_momentum_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """添加动量类指标"""
    df = df.copy()

    # RSI
    df["rsi_14"] = ta.RSI(df["close"].values, timeperiod=14)
    df["rsi_7"] = ta.RSI(df["close"].values, timeperiod=7)

    # 随机震荡器 Stochastic
    df["K"], df["D"] = ta.STOCH(
        df["high"].values,
        df["low"].values,
        df["close"].values,
        fastk_period=9,
        slowk_period=3,
        slowk_matype=0,
        slowd_period=3,
        slowd_matype=0,
    )
    df["J"] = 3 * df["K"] - 2 * df["D"]

    logger.info("⚡ 动量类指标计算完成：RSI,KDJ")
    return df


def add_volatility_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """添加波动率指标"""
    df = df.copy()

    # 布林带 (Bollinger Bands)
    df["bb_upper"], df["bb_middle"], df["bb_lower"] = ta.BBANDS(
        df["close"].values, timeperiod=20, nbdevup=2, nbdevdn=2, matype=0
    )

    logger.info("📉 波动类指标计算完成：Bollinger Bands")
    return df


def add_volume_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """添加成交量相关指标"""
    df = df.copy()

    # OBV（能量潮）
    df["obv"] = ta.OBV(df["close"].values, df["volume"].values)

    logger.info("📊 量能类指标计算完成：OBV")
    return df


def add_all_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """
    一键添加所有技术指标
    """
    logger.info("🔧 开始计算全部技术指标...")

    df = add_trend_indicators(df)
    df = add_momentum_indicators(df)
    # df = add_volatility_indicators(df)
    # df = add_volume_indicators(df)

    logger.success(f"✅ 所有技术指标添加完成，共新增 {len(df.columns) - 11} 个字段")
    return df
