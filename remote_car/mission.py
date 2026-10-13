from __future__ import annotations

import json
from pathlib import Path
from pymavlink import mavutil


class MissionError(ValueError):
    pass


def load_mission(path: str | Path) -> list[dict]:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(data, list) or not data:
        raise MissionError("Mission must be a non-empty JSON array")

    for i, wp in enumerate(data):
        if not isinstance(wp, dict):
            raise MissionError(f"Waypoint {i} must be an object")
        for key in ("lat", "lon"):
            if key not in wp:
                raise MissionError(f"Waypoint {i} missing {key}")
        lat = float(wp["lat"])
        lon = float(wp["lon"])
        if not -90 <= lat <= 90:
            raise MissionError(f"Waypoint {i} latitude out of range")
        if not -180 <= lon <= 180:
            raise MissionError(f"Waypoint {i} longitude out of range")

    return data


def upload_mission(master, waypoints: list[dict], timeout: float = 10.0) -> None:
    target_system = master.target_system
    target_component = master.target_component

    master.mav.mission_clear_all_send(target_system, target_component)
    master.mav.mission_count_send(target_system, target_component, len(waypoints))

    sent = set()
    while len(sent) < len(waypoints):
        req = master.recv_match(
            type=["MISSION_REQUEST_INT", "MISSION_REQUEST"],
            blocking=True,
            timeout=timeout,
        )
        if req is None:
            raise TimeoutError("Timed out waiting for mission request")

        seq = int(req.seq)
        if not 0 <= seq < len(waypoints):
            raise MissionError(f"Autopilot requested invalid waypoint index {seq}")

        wp = waypoints[seq]
        master.mav.mission_item_int_send(
            target_system,
            target_component,
            seq,
            mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT_INT,
            mavutil.mavlink.MAV_CMD_NAV_WAYPOINT,
            0,
            1,
            0, 0, 0, 0,
            int(float(wp["lat"]) * 1e7),
            int(float(wp["lon"]) * 1e7),
            float(wp.get("alt", 0.0)),
        )
        sent.add(seq)

    ack = master.recv_match(type="MISSION_ACK", blocking=True, timeout=timeout)
    if ack is None:
        raise TimeoutError("No MISSION_ACK received")
    if int(ack.type) != mavutil.mavlink.MAV_MISSION_ACCEPTED:
        raise MissionError(f"Mission rejected with code {ack.type}")
