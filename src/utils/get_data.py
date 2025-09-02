# src/get_data.py
import akshare as ak
import pandas as pd
from loguru import logger

def get_stock_data(code:str = 601818) -> pd.DataFrame:
    """
    获取A股个股前复权行情数据，通过config.yaml传入配置
    :return: pandas.DataFrame
    """
    try:
        logger.info(f"📡 正在获取股票 {code} 数据...")
        df = ak.stock_zh_a_hist(code,"daily",adjust="qfq")
        if df.empty:
            raise ValueError(f"未获取到股票 {code} 的数据，请检查股票代码或日期范围")

        column_mapping = {
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

        df["volume"] = df["volume"].astype("float64")
        logger.success(f"✅ 成功获取股票 {code} 数据 ({len(df)} 行)")
        return df

    except Exception as e:
        logger.error(f"❌ 获取股票 {code} 数据失败: {e}")
        return pd.DataFrame()
