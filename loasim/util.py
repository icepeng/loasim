from typing import Any, Dict

import yaml


def save_config(filename: str, obj: Dict[str, Any]):
    with open(
        filename,
        mode="w",
        encoding="utf8",
    ) as f:
        yaml.safe_dump(obj, f, allow_unicode=True, sort_keys=False)


def load_config(filename: str):
    with open(
        filename,
        encoding="utf8",
    ) as f:
        return yaml.safe_load(f)
