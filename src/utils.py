import pandas as pd
from pathlib import Path
from loguru import logger
from .config_manager import load_config

def save_dataframe_to_processed(df: pd.DataFrame, filename: str, format: str = "csv"):
    """
    将 DataFrame 保存到 /data/processed 目录下。

    Args:
        df (pd.DataFrame): 要保存的 DataFrame。
        filename (str): 文件名（不包含路径和扩展名）。
        format (str): 保存格式，可选 "parquet" 或 "csv"。默认为 "parquet"。
    """
    config = load_config()
    processed_save_path = config["processed_path"]

    processed_save_path.mkdir(parents=True, exist_ok=True)
    file_path = processed_save_path / f"{filename}.{format}"

    if format == "parquet":
        df.to_parquet(file_path, index=True) # index=True 保存日期索引
    elif format == "csv":
        df.to_csv(file_path, index=True) # index=True 保存日期索引
    else:
        logger.error(f"❌ 不支持的保存格式: {format}。请选择 'parquet' 或 'csv'。")
        return

    logger.success(f"💾 处理后已成功保存至: {file_path}")


def save_dataframe_to_raw(df: pd.DataFrame, filename: str, format: str = "csv"):
    """
    将 DataFrame 保存到 /data/processed 目录下。

    Args:
        df (pd.DataFrame): 要保存的 DataFrame。
        filename (str): 文件名（不包含路径和扩展名）。
        format (str): 保存格式，可选 "parquet" 或 "csv"。默认为 "parquet"。
    """
    config = load_config()
    raw_save_path = config["raw_path"]

    raw_save_path.mkdir(parents=True, exist_ok=True)
    file_path = raw_save_path / f"{filename}.{format}"

    if format == "parquet":
        df.to_parquet(file_path, index=True) # index=True 保存日期索引
    elif format == "csv":
        df.to_csv(file_path, index=True) # index=True 保存日期索引
    else:
        logger.error(f"❌ 不支持的保存格式: {format}。请选择 'parquet' 或 'csv'。")
        return

    logger.success(f"💾 原始数据已成功保存至: {file_path}")

