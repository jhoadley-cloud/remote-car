from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any
import yaml


class ConfigError(ValueError):
    pass


@dataclass(frozen=True)
class VehicleConfig:
    name: str
    battery_cells: int
    low_voltage_per_cell: float
    critical_voltage_per_cell: float
    max_test_speed_mps: float
    steering_output: int
    throttle_output: int
    require_gps_fix: bool
    min_satellites: int
    max_hdop: float

    @property
    def low_voltage(self) -> float:
        return self.battery_cells * self.low_voltage_per_cell

    @property
    def critical_voltage(self) -> float:
        return self.battery_cells * self.critical_voltage_per_cell


def _require(data: dict[str, Any], key: str) -> Any:
    if key not in data:
        raise ConfigError(f"Missing required key: {key}")
    return data[key]


def load_config(path: str | Path) -> VehicleConfig:
    data = yaml.safe_load(Path(path).read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ConfigError("Config root must be a mapping")

    cfg = VehicleConfig(
        name=str(_require(data, "name")),
        battery_cells=int(_require(data, "battery_cells")),
        low_voltage_per_cell=float(_require(data, "low_voltage_per_cell")),
        critical_voltage_per_cell=float(_require(data, "critical_voltage_per_cell")),
        max_test_speed_mps=float(_require(data, "max_test_speed_mps")),
        steering_output=int(_require(data, "steering_output")),
        throttle_output=int(_require(data, "throttle_output")),
        require_gps_fix=bool(_require(data, "require_gps_fix")),
        min_satellites=int(_require(data, "min_satellites")),
        max_hdop=float(_require(data, "max_hdop")),
    )
    validate_config(cfg)
    return cfg


def validate_config(cfg: VehicleConfig) -> None:
    errors: list[str] = []

    if cfg.battery_cells not in {2, 3, 4, 6}:
        errors.append("battery_cells must be one of 2, 3, 4, 6")
    if not 3.0 <= cfg.critical_voltage_per_cell <= 3.7:
        errors.append("critical_voltage_per_cell must be between 3.0 and 3.7 V")
    if not cfg.critical_voltage_per_cell < cfg.low_voltage_per_cell <= 4.2:
        errors.append("low_voltage_per_cell must be above critical and <= 4.2 V")
    if not 0.1 <= cfg.max_test_speed_mps <= 5.0:
        errors.append("max_test_speed_mps must be between 0.1 and 5.0")
    if cfg.steering_output == cfg.throttle_output:
        errors.append("steering_output and throttle_output must differ")
    if not 1 <= cfg.steering_output <= 14:
        errors.append("steering_output must be between 1 and 14")
    if not 1 <= cfg.throttle_output <= 14:
        errors.append("throttle_output must be between 1 and 14")
    if not 4 <= cfg.min_satellites <= 40:
        errors.append("min_satellites must be between 4 and 40")
    if not 0.5 <= cfg.max_hdop <= 10:
        errors.append("max_hdop must be between 0.5 and 10")

    if errors:
        raise ConfigError("; ".join(errors))
