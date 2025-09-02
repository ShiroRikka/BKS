# src/data_loader.py
import akshare as ak
import pandas as pd
from loguru import logger

from .config_manager import load_config
from .utils import save_dataframe_to_raw


def get_stock_data() -> pd.DataFrame:
    """
    获取A股个股前复权行情数据，通过config.yaml传入配置
    :return: pandas.DataFrame
    """
    config = load_config()

    symbol = config["symbol"]
    adjust = config["adjust"]
    period = config["period"]
    start_date = config["start_date"]
    end_date = config["end_date"]

    try:
        logger.info(f"📡 正在获取股票 {symbol} 数据...")
        df = ak.stock_zh_a_hist(
            symbol=symbol,
            period=period,
            start_date=start_date,
            end_date=end_date,
            adjust=adjust,
        )
        if df.empty:
            raise ValueError(f"未获取到股票 {symbol} 的数据，请检查股票代码或日期范围")

        # 保存原始数据
        filename = f"{symbol}_{adjust}_{period}"
        save_dataframe_to_raw(df, filename, format="csv")

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
        logger.success(f"✅ 成功获取股票 {symbol} 数据 ({len(df)} 行)")
        return df

    except Exception as e:
        logger.error(f"❌ 获取股票 {symbol} 数据失败: {e}")
        return pd.DataFrame()
