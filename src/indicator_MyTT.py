# src/indicator.py
import pandas as pd
from loguru import logger

from .MyTT import KDJ, MACD, RSI, BOLL, OBV
from .config_manager import load_config


def add_trend_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """添加趋势类指标"""

    # MACD
    df["MACD_DIF"], df["MACD_DEA"], df["MACD_M"] = MACD(df["close"].values, 12, 26, 9)

    logger.info("📈 MACD 计算完成")
    return df


def add_rsi_indicator(df: pd.DataFrame) -> pd.DataFrame:
    df["rsi_14"] = RSI(df["close"].values, 14)
    df["rsi_7"] = RSI(df["close"].values, 7)
    logger.info("⚡ RSI 计算完成")
    return df


def add_kdj_indicator(df: pd.DataFrame) -> pd.DataFrame:
    df["K"], df["D"], df["J"] = KDJ(
        df["close"].values, df["high"].values, df["low"].values, 9, 3, 3
    )
    logger.info("⚡ KDJ 计算完成")
    return df


def add_volatility_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """添加波动率指标"""

    # 布林带 (Bollinger Bands)
    df["bb_upper"], df["bb_middle"], df["bb_lower"] = BOLL(df["close"].values, 20, 2)

    logger.info("📉 布林带 计算完成")
    return df


def add_volume_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """添加成交量相关指标"""

    # OBV（能量潮）
    df["obv"] = OBV(df["close"].values, df["volume"].values)

    logger.info("📊 OBV 计算完成")
    return df


def add_all_indicators(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    config = load_config()["features"]

    if config.get("include_macd"):
        df = add_trend_indicators(df)
    if config.get("include_rsi"):
        df = add_rsi_indicator(df)
    if config.get("include_kdj"):
        df = add_kdj_indicator(df)
    if config.get("include_boll"):
        df = add_volatility_indicators(df)
    if config.get("include_obv"):
        df = add_volume_indicators(df)

    logger.success(f"✅ 所有技术指标添加完成，当前列数: {len(df.columns)}")
    return df
