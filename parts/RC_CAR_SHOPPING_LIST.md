# RC Car Shopping List

This list tracks parts still needed for the Pixhawk-based rover. Items already confirmed as owned are excluded from the main buy list unless the owned item is not suitable for V1.

## V1 target

- 1/10-scale 4WD crawler / trail-truck layout
- Conventional steering servo
- Low-speed controllable drivetrain
- Pixhawk 2.4.8 running ArduRover
- Manual RC control first, GPS autonomy later
- Splash / rain / wet-grass resistance
- Initial autonomous test speed around 1 m/s

## Must buy or select

| Priority | Item | Target / requirement | Qty | Budget | Candidate / brand | Status | Notes |
|---|---|---|---:|---:|---|---|---|
| 1 | 1/10 4WD crawler/trail chassis | Room for battery + sealed Pixhawk box; standard steering servo mount | 1 | TBD | TBD | Researching | Chassis choice drives most dimensions |
| 1 | Brushed motor | 540/550, roughly 27T-35T starting point | 1 | TBD | TBD | Researching | Prioritize low-speed control |
| 1 | Rover ESC | Waterproof, brushed, forward/brake/reverse, 2S-compatible | 1 | TBD | TBD | Researching | Owned 60A 2S-6S ESC may be unsuitable if brushless/aircraft-only |
| 1 | Steering servo | Waterproof, metal gear, roughly 20-30 kg-cm | 1 | TBD | TBD | Researching | Owned micro servos are not assumed sufficient |
| 1 | 2S hardcase LiPo | Around 5000 mAh, sized to chassis | 1-2 | TBD | TBD | Researching | Owned 6S 3200 mAh pack is not the default V1 choice |
| 1 | LiPo balance charger | Balance + storage charge, supports chosen battery | 1 | TBD | TBD | Researching | Only if current charger inventory does not cover this |
| 1 | RC transmitter | At least 6 useful channels | 1 | TBD | TBD | Researching | Need mode, HOLD, arm/disarm controls |
| 1 | RC receiver | Compatible with transmitter and Pixhawk | 1 | TBD | TBD | Researching | Prefer SBUS/PPM/supported serial |
| 1 | Pixhawk power module | Compatible with 2.4.8 and drivetrain current | 1 | TBD | TBD | Researching | First inspect owned Pixhawk bundle |
| 1 | GPS + compass | ArduPilot-compatible external module | 1 | TBD | TBD | Researching | First inspect owned Pixhawk bundle |
| 1 | Waterproof electronics box | Gasketed enclosure for Pixhawk + receiver | 1 | TBD | TBD | Researching | Size after chassis and internal layout |
| 1 | Cable glands | Match actual wire diameters | Assorted | TBD | TBD | Researching | Side/downward exits preferred |
| 1 | Main fuse + holder | Size after measuring real drivetrain current | 1 + spares | TBD | TBD | Researching | |
| 1 | Servo BEC | 5-6 V, high-current if ESC BEC is insufficient | 1 | TBD | TBD | Researching | Decision depends on servo + ESC |
| 2 | Waterproofing supplies | Dielectric grease, adhesive marine heat-shrink, electronics-safe silicone | Assorted | TBD | TBD | Researching | Standard heat-shrink already owned |
| 2 | Mounting hardware | M2/M2.5/M3 hardware, washers, lock nuts, threaded inserts | Assorted | TBD | TBD | Researching | Buy after chassis/enclosure selection |
| 2 | Vibration isolation | Foam/gel/rubber mount for Pixhawk | 1 set | TBD | TBD | Researching | |
| 2 | Desiccant + moisture indicators | For enclosure testing | Assorted | TBD | TBD | Researching | |
| 3 | Telemetry radio | MAVLink field tuning | 1 set | TBD | TBD | Optional | Check Pixhawk bundle before buying |
| 3 | Lidar/rangefinder | Obstacle sensing | 1 | TBD | TBD | Post-V1 | Only after GPS navigation works |
| 3 | Wheel encoders | Odometry | 2+ | TBD | TBD | Post-V1 | |

## Already owned and likely useful

- Pixhawk 2.4.8 bundle, exact accessories TBD
- Raspberry Pi 4 Model B, 2 GB
- CMUcam5 Pixy
- M5Stack Timer Camera X
- 2x Inland ESP32-CAM
- AMG883x thermal sensor
- DSD TECH Bluetooth UART module
- XT60 / IC5 / EC5 cable assortment
- Dupont 2.54 mm to JST-SH 1.0 mm signal cables
- PCB prototyping boards, breadboard, jumper wires
- 20x 1000 µF capacitors
- assorted resistors
- multimeter
- soldering setup
- heat gun + heat-shrink
- calipers
- wire strippers
- tools
- 3D printer + filament

## Decisions before ordering

1. Pick the chassis.
2. Inventory the Pixhawk bundle.
3. Confirm whether the owned 60A 2S-6S ESC is brushed or brushless and whether it has reverse + usable BEC.
4. Select motor and battery around the chassis.
5. Verify servo current and ESC BEC capability.
6. Lock the high-current connector standard.
7. Measure enclosure and mounting geometry.
