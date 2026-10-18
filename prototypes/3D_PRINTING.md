# 3D Printing Prototype Index

Use this file to track printable reference models, prototype downloads, and custom CAD for both the RC rover and future drone.

## Rules for prototypes

- Treat internet models as references until dimensions are checked.
- Prefer STEP/F3D files over STL when available because they are easier to modify.
- Do not print chassis-specific mounts until the chassis/frame is selected.
- For outdoor vehicle parts, prefer PETG/ASA or another suitable material over PLA where heat/water exposure matters.
- Flexible antenna/GPS mounts are often better in TPU.
- Record license/attribution requirements before remixing or committing derivative geometry.

## Download / reference candidates

| Project | Candidate | What it helps with | Fit status | Source |
|---|---|---|---|---|
| Rover / general | Pixhawk 2.1 mounting template by Fickert | Pixhawk footprint and mounting reference | Reference only; 2.4.8 dimensions must be verified | https://www.thingiverse.com/thing:2013466 |
| Rover / general | Anti-vibration Pixhawk mount for Bix3 | Reference for vibration-isolated FC mounting | Reference only; aircraft-specific base | https://www.thingiverse.com/thing:1878696 |
| Rover | Tarmo5 electronics box and cover Mk.2 | Reference for RC electronics enclosure layout and serviceable lid | Chassis-specific; remix/reference | https://www.printables.com/model/433105-tarmo5-electronics-box-and-cover-mk2 |
| Rover | WPL C14/24 V3 PCB electronics tray | Reference for simple removable electronics tray | Chassis-specific | https://www.thingiverse.com/thing:4789353/files |
| Rover | SCX10-family 3S battery tray | Reference for low-mounted crawler battery tray | Only useful if selected chassis is SCX10-compatible | https://www.printables.com/model/813074-3s-battery-tray-for-scx10-scx10ii-scx10iii |
| Rover | SCX24 low-CG battery tray | Reference for battery-retention geometry | Wrong scale for planned 1/10 V1; geometry reference only | https://www.printables.com/model/236070-scx24-low-cg-battery-tray-v1 |
| Drone | AX540 hexacopter frame | Full printable large hexacopter reference | Possible future architecture; requires large printer/build volume and separate sizing analysis | https://www.printables.com/model/1165926-ax540-hexacopter-frame |
| Drone | FlyFishRC VX3.5 GPS mount | GPS mount with STL/F3Z/STEP files | Frame-specific; useful CAD reference | https://www.printables.com/model/1067241-flyfishrc-vx35-gps/files |
| Drone | Volador VX5 GPS mount for 21x21 mm modules | TPU GPS mounting concept | Frame-specific; useful if GPS is 21x21 mm | https://www.printables.com/model/877265-volador-vx5-t700-gps-mount-hglrc-m100-5883-and-oth |
| Drone | SpeedyBee Master 5 V2 GPS/compass mount | Level GPS/compass mounting concept | Frame + GPS specific; useful design reference | https://www.printables.com/model/1485002-speedybee-maser-5-v2-mateksys-m10q-5883-gps-compas |
| Drone | TBS Source One V5 receiver tray | Small receiver tray mounting concept | Frame-specific | https://www.printables.com/model/315216-rc-rx-mounting-tray-tbs-source-one-v5 |

## Rover custom CAD queue

These should probably be designed around the actual chassis rather than downloaded blindly.

| Prototype | Inputs needed | First prototype goal | Status |
|---|---|---|---|
| Pixhawk electronics tray | Pixhawk dimensions, enclosure internal dimensions, cable exits | Secure controller with removable vibration mounts | Waiting on measurements |
| Waterproof enclosure bracket | Chassis rail/deck dimensions, enclosure size | Rigid mount with fast removal | Waiting on chassis |
| GPS/compass mast | GPS module dimensions, chassis mounting points | Keep module level and separated from high-current wiring | Waiting on GPS/chassis |
| RC receiver mount | Receiver dimensions | Secure receiver + antenna strain relief | Waiting on receiver |
| Antenna mounts | Antenna lengths/diameters | Protected orientation with replaceable clips | Waiting on radio |
| Battery tray/retainer | Battery dimensions, chassis | Low-CG retention with strap | Waiting on battery/chassis |
| Cable gland support plate | Gland thread sizes, enclosure wall thickness | Reinforce wall and organize exits | Waiting on enclosure |
| Pixy / camera mount | Camera choice + FOV target | Adjustable front-facing sensor mount | Optional |
| Raspberry Pi tray | Pi cooling/enclosure plan | Companion-computer mount separate from Pixhawk | Post-V1 |
| Lidar bracket | Sensor choice | Level front-facing rangefinder mount | Post-V1 |

## Drone custom CAD queue

| Prototype | Inputs needed | First prototype goal | Status |
|---|---|---|---|
| Pixhawk vibration mount | Frame stack dimensions, Pixhawk footprint | Isolate FC while retaining access | Waiting on frame |
| GPS/compass mast | GPS dimensions + frame geometry | Level module away from power wiring | Waiting on frame/GPS |
| Receiver/telemetry tray | Radio modules + frame | Organized low-mass mounting | Waiting on electronics |
| Camera mount | Camera selection + desired angle | Protected adjustable camera | Optional |
| Raspberry Pi mount | Pi use case + frame payload allowance | Rigid, cooled companion-computer mount | Optional |
| Landing gear | Prop/frame clearance + payload | Stable takeoff/landing and sensor clearance | Waiting on frame |
| Fog-flow test fixture | Motor/prop geometry | Safe bench fixture for smoke-flow visualization | Researching |

## First prototype sequence

1. Select the rover chassis.
2. Measure the Pixhawk and inventory its bundled GPS/power hardware.
3. Lay the major rover components physically on the chassis.
4. CAD a simple electronics tray before attempting a fully sealed enclosure.
5. Print in inexpensive filament for fit checks.
6. Revise clearances and wire routing.
7. Move final wet-environment parts to a more appropriate filament.
8. Repeat the same process for the drone only after its frame architecture is selected.
