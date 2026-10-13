# Build Plan

## V1 goal

Build a 1/10-scale 4WD rover that is manually drivable, conservatively speed-limited during development, GPS-navigation capable, resistant to rain/wet grass/shallow splashes, and always recoverable by human RC intervention.

## Phase 0: validate Pixhawk

- Connect Pixhawk 2.4.8 by USB.
- Flash ArduPilot Rover using the appropriate Pixhawk1 target.
- Confirm gyro, accelerometer, compass, SD logging, RC input, and outputs.
- Reject the board if persistent sensor faults remain.

Exit criteria:
- clean boot
- heartbeat present
- SD logs written
- receiver channels move correctly
- output rail verified with wheels off ground

## Phase 1: conventional RC chassis

Recommended:
- 1/10 4WD crawler/trail chassis
- 27T-35T brushed 540/550 motor
- waterproof reversible brushed ESC
- waterproof metal-gear servo
- 2S hardcase LiPo

Run it temporarily as a conventional RC car before adding Pixhawk.

Exit criteria:
- no drivetrain binding
- neutral does not creep
- forward/reverse/brake correct
- acceptable motor/ESC temperature
- steering linkage does not bind

## Phase 2: Pixhawk integration

Wire:
- receiver -> RC IN or supported serial port
- MAIN OUT 1 -> steering servo
- MAIN OUT 3 -> ESC signal
- power module -> POWER
- GPS/compass -> appropriate GPS/compass interfaces

Configure:
- radio calibration
- servo functions
- steering direction/endpoints
- throttle direction/endpoints
- battery monitor
- RC-loss failsafe -> HOLD
- low battery -> HOLD
- emergency switch -> HOLD

## Phase 3: manual driving

Start below 1 m/s where practical.

Tests:
1. 5 m straight
2. repeated stop/start
3. full-lock low-speed turns
4. reverse
5. RC-loss failsafe
6. 10 minute thermal test
7. log review

## Phase 4: waterproofing

- gasketed electronics box
- downward-facing cable glands
- drip loops
- dielectric grease on external connectors
- marine heat-shrink on splices
- waterproof ESC outside sealed box for cooling
- desiccant inside enclosure

## Phase 5: navigation

Order:
1. HOLD
2. MANUAL
3. STEERING
4. GUIDED short move
5. one waypoint
6. four-waypoint rectangle
7. RTL
8. larger geofence-limited missions

Use a large empty field and keep early autonomous speed near walking pace.

## Phase 6: later upgrades

- lidar obstacle sensing
- wheel encoders
- companion computer
- FPV
- lights
- telemetry radio
- faster drivetrain only after controls and failsafes are proven
