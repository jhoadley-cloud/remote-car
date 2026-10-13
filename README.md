# remote-car

A waterproof-capable 1/10-scale RC rover built around a Pixhawk 2.4.8 running ArduPilot Rover.

This repository contains software, configuration templates, safety tooling, wiring notes, commissioning procedures, and a staged build plan.

> **Safety:** Keep the vehicle restrained or the wheels off the ground during bench testing. Configure RC-loss and battery failsafes before outdoor operation. Never test autonomous modes near roads, people, pets, or property.

## Architecture

- **Pixhawk 2.4.8 / Pixhawk1 target**: steering, throttle, sensor fusion, failsafes, geofence, navigation
- **ArduPilot Rover**: vehicle-control firmware
- **RC receiver**: manual control and emergency intervention
- **GPS + compass**: navigation
- **Python tools**: configuration validation, preflight checks, telemetry logging, mission upload, emergency Hold
- **Mission Planner**: firmware installation and first-time calibration

## Recommended V1 hardware

- 1/10 4WD crawler/trail chassis
- 540/550 brushed motor, about 27T-35T
- waterproof brushed ESC with reverse
- waterproof metal-gear steering servo
- 2S hardcase LiPo
- Pixhawk-compatible power module sized for drivetrain current
- external GPS/compass
- 6+ channel radio
- gasketed electronics enclosure with cable glands
- separate servo BEC if needed

## Quick start

1. Read `docs/BUILD_PLAN.md`.
2. Wire the vehicle using `docs/WIRING.md`.
3. Flash ArduPilot Rover to the Pixhawk and perform first-time calibration.
4. Copy `configs/vehicle.example.yaml` to `vehicle.yaml`.
5. Install:

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -e ".[dev]"
```

6. Run:

```bash
pytest
remote-car config-check --config vehicle.yaml
```

7. Connect by USB:

```bash
remote-car preflight --connection COM5 --config vehicle.yaml
```

8. Complete `docs/COMMISSIONING.md` before driving.

## CLI

```text
remote-car config-check --config vehicle.yaml
remote-car preflight --connection COM5 --config vehicle.yaml
remote-car telemetry --connection COM5 --output logs/session.csv
remote-car upload-mission --connection COM5 --mission missions/test_rectangle.json
remote-car emergency-stop --connection COM5
```

## Status

Initial engineering baseline. Hardware-specific PWM directions/endpoints, current-sensor calibration, steering geometry, and navigation tuning must be verified on the physical vehicle.
