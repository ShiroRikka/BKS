import akshare as ak
import pandas as pd
from loguru import logger


def get_stock_data(code: str = "601818") -> pd.DataFrame:
    """
    获取A股个股前复权行情数据。

    Args:
        code (str, optional): 股票代码. Defaults to "601818".

    Returns:
        pd.DataFrame: 包含股票数据的DataFrame，如果获取失败则返回一个空的DataFrame。
    """
    try:
        logger.info(f"📡 正在获取股票 {code} 数据...")
        df = ak.stock_zh_a_hist(symbol=code, period="daily", adjust="qfq")
        if df.empty:
            raise ValueError(f"未获取到股票 {code} 的数据，请检查股票代码是否正确")

        column_mapping = {
            "股票代码": "code",
            "日期": "date",
            "开盘": "open",
            "收盘": "close",
            "最高": "high",
            "最低": "low",
            "成交量": "volume",
            "成交额": "amount",
            "振幅": "amplitude",
            "涨跌幅": "pct_change",
            "涨跌额": "change",
            "换手率": "turnover",
        }
        df = df.rename(columns=column_mapping)
        df["date"] = pd.to_datetime(df["date"])
        df = df.set_index("date").sort_index()

        # 选择需要保留的列
        columns_to_keep = ["code", "open", "close", "high", "low", "volume"]
        df = df[columns_to_keep].copy()  # 使用.copy()避免SettingWithCopyWarning

        df["volume"] = df["volume"].astype("float64")
        logger.success(f"✅ 成功获取股票 {code} 数据 ({len(df)} 行)")
        return df

    except Exception as e:
        logger.error(f"❌ 获取股票 {code} 数据失败: {e}")
        return pd.DataFrame()
