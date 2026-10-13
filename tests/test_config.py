import pytest
from remote_car.config import VehicleConfig, ConfigError, validate_config


def good():
    return VehicleConfig(
        name="test",
        battery_cells=2,
        low_voltage_per_cell=3.55,
        critical_voltage_per_cell=3.35,
        max_test_speed_mps=1.0,
        steering_output=1,
        throttle_output=3,
        require_gps_fix=True,
        min_satellites=8,
        max_hdop=2.0,
    )


def test_valid_config():
    validate_config(good())


def test_outputs_must_differ():
    config = good()
    config = VehicleConfig(**(config.__dict__ | {"throttle_output": 1}))
    with pytest.raises(ConfigError):
        validate_config(config)


def test_voltage_ordering():
    config = good()
    config = VehicleConfig(**(config.__dict__ | {"low_voltage_per_cell": 3.2}))
    with pytest.raises(ConfigError):
        validate_config(config)
