# src/config_manager.py
import yaml
from loguru import logger
from pathlib import Path # 确保导入 Path

# 建议 config_file 类型为 Path，并设置默认值
def load_config(config_file: Path = Path("config/config.yaml")):
    """读取 yaml 配置并拆包返回常用字段"""
    with open(config_file, "r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)
        logger.info(f"✅ 配置文件已加载: {config_file}")
        stock = cfg["stock"]
        save_path = cfg["save_path"]
        return (
            stock["symbol"],
            stock["adjust"],
            stock["period"],
            stock["start_date"],
            stock["end_date"],
            Path(save_path["raw"]),       # 转换为 Path 对象
            Path(save_path["processed"])   # 转换为 Path 对象
        )

