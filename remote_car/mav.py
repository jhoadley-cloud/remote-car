from __future__ import annotations

from contextlib import contextmanager
from pymavlink import mavutil


@contextmanager
def mavlink_connection(connection: str, baud: int = 115200, timeout: float = 10.0):
    master = mavutil.mavlink_connection(connection, baud=baud)
    hb = master.wait_heartbeat(timeout=timeout)
    if hb is None:
        raise TimeoutError(f"No MAVLink heartbeat received from {connection}")
    try:
        yield master
    finally:
        try:
            master.close()
        except Exception:
            pass


def set_mode(master, mode_name: str) -> None:
    mapping = master.mode_mapping()
    if not mapping or mode_name.upper() not in mapping:
        raise ValueError(f"Mode {mode_name!r} is unavailable")
    master.set_mode(mapping[mode_name.upper()])


def emergency_hold(master) -> None:
    set_mode(master, "HOLD")
