from __future__ import annotations

import csv
from datetime import datetime, timezone
from pathlib import Path

FIELDS = [
    "timestamp_utc", "type", "lat_deg", "lon_deg", "alt_m",
    "groundspeed_mps", "heading_deg", "battery_v", "current_a",
]


def _row_from_message(msg):
    typ = msg.get_type()
    row = {k: "" for k in FIELDS}
    row["timestamp_utc"] = datetime.now(timezone.utc).isoformat()
    row["type"] = typ

    if typ == "GLOBAL_POSITION_INT":
        row["lat_deg"] = getattr(msg, "lat", 0) / 1e7
        row["lon_deg"] = getattr(msg, "lon", 0) / 1e7
        row["alt_m"] = getattr(msg, "relative_alt", 0) / 1000.0
        row["groundspeed_mps"] = getattr(msg, "vx", 0) / 100.0
        hdg = getattr(msg, "hdg", 65535)
        row["heading_deg"] = "" if hdg == 65535 else hdg / 100.0

    elif typ == "SYS_STATUS":
        voltage = getattr(msg, "voltage_battery", 65535)
        current = getattr(msg, "current_battery", -1)
        row["battery_v"] = "" if voltage == 65535 else voltage / 1000.0
        row["current_a"] = "" if current < 0 else current / 100.0

    return row


def log_telemetry(master, output: str | Path) -> None:
    path = Path(output)
    path.parent.mkdir(parents=True, exist_ok=True)
    new_file = not path.exists()

    with path.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        if new_file:
            writer.writeheader()

        while True:
            msg = master.recv_match(
                type=["GLOBAL_POSITION_INT", "SYS_STATUS"],
                blocking=True,
                timeout=1,
            )
            if msg is not None:
                writer.writerow(_row_from_message(msg))
                f.flush()
