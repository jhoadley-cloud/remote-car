from __future__ import annotations

import argparse
import json
from .config import load_config
from .mav import mavlink_connection, emergency_hold
from .mission import load_mission, upload_mission
from .preflight import run_preflight
from .telemetry import log_telemetry


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="remote-car")
    sub = parser.add_subparsers(dest="command", required=True)

    config = sub.add_parser("config-check")
    config.add_argument("--config", required=True)

    preflight = sub.add_parser("preflight")
    preflight.add_argument("--connection", required=True)
    preflight.add_argument("--baud", type=int, default=115200)
    preflight.add_argument("--config", required=True)

    telemetry = sub.add_parser("telemetry")
    telemetry.add_argument("--connection", required=True)
    telemetry.add_argument("--baud", type=int, default=115200)
    telemetry.add_argument("--output", required=True)

    mission = sub.add_parser("upload-mission")
    mission.add_argument("--connection", required=True)
    mission.add_argument("--baud", type=int, default=115200)
    mission.add_argument("--mission", required=True)

    stop = sub.add_parser("emergency-stop")
    stop.add_argument("--connection", required=True)
    stop.add_argument("--baud", type=int, default=115200)

    return parser


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)

    if args.command == "config-check":
        cfg = load_config(args.config)
        print(json.dumps(
            cfg.__dict__ | {
                "low_voltage": cfg.low_voltage,
                "critical_voltage": cfg.critical_voltage,
            },
            indent=2,
        ))
        return 0

    if args.command == "preflight":
        cfg = load_config(args.config)
        with mavlink_connection(args.connection, args.baud) as master:
            results = run_preflight(master, cfg)
        for result in results:
            print(f"[{'PASS' if result.passed else 'FAIL'}] {result.name}: {result.detail}")
        return 0 if all(result.passed for result in results) else 2

    if args.command == "telemetry":
        with mavlink_connection(args.connection, args.baud) as master:
            log_telemetry(master, args.output)
        return 0

    if args.command == "upload-mission":
        mission = load_mission(args.mission)
        with mavlink_connection(args.connection, args.baud) as master:
            upload_mission(master, mission)
        print(f"Uploaded {len(mission)} waypoints")
        return 0

    if args.command == "emergency-stop":
        with mavlink_connection(args.connection, args.baud) as master:
            emergency_hold(master)
        print("HOLD mode requested")
        return 0

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
