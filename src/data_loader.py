import akshare as ak
import pandas as pd
import yaml
from loguru import logger


def load_config(config_file: str = "config/config.yaml"):
    """读取 yaml 配置并拆包返回常用字段"""
    with open(config_file, "r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)
        logger.info(f"✅ 配置文件已加载: {config_file}")
        stock = cfg["stock"]
        return (
            stock["symbol"],
            stock["adjust"],
            stock["period"],
            stock["start_date"],
            stock["end_date"],
        )


def get_stock_data() -> pd.DataFrame:
    """
    获取A股个股前复权行情数据，通过config.yaml传入配置
    :return: pandas.DataFrame
    """
    symbol, adjust, period, start_date, end_date = load_config()
    try:
        df = ak.stock_zh_a_hist(
            symbol=symbol,
            period=period,
            start_date=start_date,
            end_date=end_date,
            adjust=adjust,
        )
        if df.empty:
            raise ValueError(f"未获取到股票 {symbol} 的数据，请检查股票代码")

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

        logger.success(f"✅ 成功获取股票 {symbol} 数据 ({len(df)} 行)")
        return df

    except Exception as e:
        logger.error(f"获取股票 {symbol} 数据失败: {e}")
        return pd.DataFrame()
