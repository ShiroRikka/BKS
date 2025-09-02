# src/utils.py
from pathlib import Path
import pandas as pd
from loguru import logger
from .config_manager import load_config


def save_dataframe_to_raw(df: pd.DataFrame, filename: str, format: str = "csv"):
    config = load_config()
    path = config["raw_path"]
    path.mkdir(parents=True, exist_ok=True)
    file_path = path / f"{filename}.{format}"

    _save_df(df, file_path, format, "原始")


def save_dataframe_to_processed(df: pd.DataFrame, filename: str, format: str = "csv"):
    config = load_config()
    path = config["processed_path"]
    path.mkdir(parents=True, exist_ok=True)
    file_path = path / f"{filename}.{format}"

    _save_df(df, file_path, format, "处理后")


def _save_df(df: pd.DataFrame, file_path: Path, format: str, desc: str):
    try:
        if format == "parquet":
            df.to_parquet(file_path, index=True)
        elif format == "csv":
            df.to_csv(file_path, index=True, encoding="utf-8-sig")
        else:
            logger.error(f"❌ 不支持的格式: {format}")
            return
        logger.info(f"💾 {desc}数据已保存: {file_path}")
    except Exception as e:
        logger.error(f"❌ 保存文件失败 {file_path}: {e}")
