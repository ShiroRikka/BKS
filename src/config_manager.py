# src/config_manager.py
from pathlib import Path  # 确保导入 Path

import yaml
from loguru import logger


# 建议 config_file 类型为 Path，并设置默认值
def load_config(config_file: Path = Path("config/config.yaml")):
    """读取 yaml 配置并拆包返回常用字段"""
    with open(config_file, "r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)
        logger.info(f"✅ 配置文件已加载: {config_file}")
        stock = cfg["stock"]
        save = cfg["save"]
        return {
            "symbol": cfg["stock"]["symbol"],
            "adjust": cfg["stock"]["adjust"],
            "period": cfg["stock"]["period"],
            "start_date": cfg["stock"]["start_date"],
            "end_date": cfg["stock"]["end_date"],
            "raw_path": Path(cfg["save"]["raw"]),
            "processed_path": Path(cfg["save"]["processed"]),
            "output_format": cfg["save"]["output_format"],
            "features": cfg.get("features", {}),
        }
