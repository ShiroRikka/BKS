# src/indicator.py
import pandas as pd
import talib as ta
from loguru import logger


def add_trend_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """添加趋势类指标"""
    df = df.copy()

    # # 简单移动平均线
    # df["ma5"] = ta.SMA(df["close"].values, timeperiod=5)
    # df["ma10"] = ta.SMA(df["close"].values, timeperiod=10)
    # df["ma20"] = ta.SMA(df["close"].values, timeperiod=20)
    # df["ma60"] = ta.SMA(df["close"].values, timeperiod=60)
    #
    # # 指数移动平均线（EMA）
    # df["ema12"] = ta.EMA(df["close"].values, timeperiod=12)
    # df["ema26"] = ta.EMA(df["close"].values, timeperiod=26)

    # MACD
    df["DIF"], df["MACE_DEA"], df["MACD_M"] = ta.MACD(
        df["close"].values, fastperiod=12, slowperiod=26, signalperiod=9
    )

    # # 抛物线转向 SAR
    # df["sar"] = ta.SAR(df["high"].values, df["low"].values, acceleration=0.02, maximum=0.2)

    logger.info("📈 趋势类指标计算完成：MA, EMA, MACD")
    # logger.info("📈 趋势类指标计算完成：MA, EMA, MACD, SAR")
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
        slowk_matype=1,
        slowd_period=3,
        slowd_matype=1,
    )
    df["J"] = 3 * df["K"] - 2 * df["D"]

    # # CCI
    # df["cci"] = ta.CCI(df["high"].values, df["low"].values, df["close"].values, timeperiod=14)
    #
    # # ROC（价格变化率）
    # df["roc"] = ta.ROC(df["close"].values, timeperiod=10)

    logger.info("⚡ 动量类指标计算完成：RSI")
    # logger.info("⚡ 动量类指标计算完成：RSI, Stochastic, CCI, ROC")
    return df


def add_volatility_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """添加波动率指标"""
    df = df.copy()

    # 布林带 (Bollinger Bands)
    df["bb_upper"], df["bb_middle"], df["bb_lower"] = ta.BBANDS(
        df["close"].values, timeperiod=20, nbdevup=2, nbdevdn=2, matype=0
    )

    # # ATR（平均真实波幅）
    # df["atr"] = ta.ATR(df["high"].values, df["low"].values, df["close"].values, timeperiod=14)

    logger.info("📉 波动类指标计算完成：Bollinger Bands")
    return df


def add_volume_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """添加成交量相关指标"""
    df = df.copy()

    # # 成交量移动平均
    # df["volume_ma5"] = ta.SMA(df["volume"].values, timeperiod=5)
    # df["volume_ma10"] = ta.SMA(df["volume"].values, timeperiod=10)

    # OBV（能量潮）
    df["obv"] = ta.OBV(df["close"].values, df["volume"].values)

    logger.info("📊 量能类指标计算完成：OBV")
    # logger.info("📊 量能类指标计算完成：Volume MA, OBV")
    return df


def add_all_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """
    一键添加所有技术指标
    """
    logger.info("🔧 开始计算全部技术指标...")

    df = add_trend_indicators(df)
    df = add_momentum_indicators(df)
    # df = add_volatility_indicators(df)
    df = add_volume_indicators(df)

    logger.success(f"✅ 所有技术指标添加完成，共新增 {len(df.columns) - 11} 个字段")
    return df
