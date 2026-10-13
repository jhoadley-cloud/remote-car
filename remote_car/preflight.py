from __future__ import annotations

from dataclasses import dataclass, asdict
from time import monotonic
from .config import VehicleConfig


@dataclass
class CheckResult:
    name: str
    passed: bool
    detail: str

    def as_dict(self) -> dict:
        return asdict(self)


def run_preflight(master, cfg: VehicleConfig, sample_seconds: float = 5.0) -> list[CheckResult]:
    battery_voltage = None
    gps_fix = None
    sats = None
    hdop = None
    heartbeat_seen = False
    system_status = None

    deadline = monotonic() + sample_seconds
    while monotonic() < deadline:
        msg = master.recv_match(blocking=True, timeout=0.5)
        if msg is None:
            continue
        typ = msg.get_type()

        if typ == "HEARTBEAT":
            heartbeat_seen = True
            system_status = int(getattr(msg, "system_status", -1))

        elif typ == "SYS_STATUS":
            mv = getattr(msg, "voltage_battery", 65535)
            if mv not in (0, 65535):
                battery_voltage = mv / 1000.0

        elif typ == "GPS_RAW_INT":
            gps_fix = int(getattr(msg, "fix_type", 0))
            sats = int(getattr(msg, "satellites_visible", 0))
            eph = int(getattr(msg, "eph", 65535))
            if eph not in (0, 65535):
                hdop = eph / 100.0

    out = [CheckResult("heartbeat", heartbeat_seen, f"system_status={system_status}")]

    if battery_voltage is None:
        out.append(CheckResult("battery", False, "No valid battery voltage received"))
    else:
        out.append(CheckResult(
            "battery",
            battery_voltage >= cfg.low_voltage,
            f"{battery_voltage:.2f} V; required >= {cfg.low_voltage:.2f} V",
        ))

    if cfg.require_gps_fix:
        out.append(CheckResult("gps_fix", gps_fix is not None and gps_fix >= 3, f"fix_type={gps_fix}; need >= 3"))
        out.append(CheckResult("satellites", sats is not None and sats >= cfg.min_satellites, f"satellites={sats}; need >= {cfg.min_satellites}"))
        out.append(CheckResult("hdop", hdop is not None and hdop <= cfg.max_hdop, f"hdop={hdop}; need <= {cfg.max_hdop}"))

    return out
