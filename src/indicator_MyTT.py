# src/indicator.py
import pandas as pd
from loguru import logger

from .config_manager import load_config
from .MyTT import KDJ, MACD, RSI, BOLL, OBV


def add_trend_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """添加趋势类指标"""
    df = df.copy()

    # MACD
    df["MACD_DIF"], df["MACD_DEA"], df["MACD_M"] = MACD(df["close"].values, 12, 26, 9)

    logger.info("📈 MACD 计算完成")
    return df


def add_momentum_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """添加动量类指标"""
    df = df.copy()

    # RSI
    df["rsi_14"] = RSI(df["close"].values, 14)
    df["rsi_7"] = RSI(df["close"].values, 7)

    # 随机震荡器 Stochastic
    df["K"], df["D"], df["J"] = KDJ(
        df["close"].values,
        df["high"].values,
        df["low"].values,
        9,
        3,
        3,
    )

    logger.info("⚡ RSI, KDJ 计算完成")
    return df


def add_volatility_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """添加波动率指标"""
    df = df.copy()

    # 布林带 (Bollinger Bands)
    df["bb_upper"], df["bb_middle"], df["bb_lower"] = BOLL(df["close"].values, 20, 2)

    logger.info("📉 布林带 计算完成")
    return df


def add_volume_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """添加成交量相关指标"""
    df = df.copy()

    # OBV（能量潮）
    df["obv"] = OBV(df["close"].values, df["volume"].values)

    logger.info("📊 OBV 计算完成")
    return df


def add_all_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """
    一键添加所有技术指标
    """
    config = load_config()["features"]

    if config.get("include_macd"): df = add_trend_indicators(df)
    if config.get("include_rsi"): df = add_momentum_indicators(df)
    if config.get("include_kdj"): df = add_momentum_indicators(df)
    if config.get("include_boll"): df = add_volatility_indicators(df)
    if config.get("include_obv"): df = add_volume_indicators(df)


    logger.success(f"✅ 所有技术指标添加完成，当前列数: {len(df.columns)}")
    return df
