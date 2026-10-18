# RC Car 3D Printing Prototype Index

Track downloadable reference models and custom CAD for the Pixhawk rover here.

## Rules for prototypes

- Treat internet models as references until dimensions are checked.
- Prefer STEP/F3D files over STL when available because they are easier to modify.
- Do not print chassis-specific mounts until the chassis is selected.
- For outdoor vehicle parts, prefer PETG/ASA or another suitable material over PLA where heat/water exposure matters.
- Flexible antenna/GPS mounts are often better in TPU.
- Record license/attribution requirements before remixing or committing derivative geometry.

## Download / reference candidates

| Candidate | What it helps with | Fit status | Source |
|---|---|---|---|
| Pixhawk 2.1 mounting template by Fickert | Pixhawk footprint and mounting reference | Reference only; 2.4.8 dimensions must be verified | https://www.thingiverse.com/thing:2013466 |
| Anti-vibration Pixhawk mount for Bix3 | Reference for vibration-isolated FC mounting | Reference only; aircraft-specific base | https://www.thingiverse.com/thing:1878696 |
| Tarmo5 electronics box and cover Mk.2 | RC electronics enclosure layout and serviceable lid | Chassis-specific; remix/reference | https://www.printables.com/model/433105-tarmo5-electronics-box-and-cover-mk2 |
| WPL C14/24 V3 PCB electronics tray | Simple removable electronics tray | Chassis-specific | https://www.thingiverse.com/thing:4789353/files |
| SCX10-family 3S battery tray | Low-mounted crawler battery tray | Useful only if selected chassis is SCX10-compatible | https://www.printables.com/model/813074-3s-battery-tray-for-scx10-scx10ii-scx10iii |
| SCX24 low-CG battery tray | Battery-retention geometry reference | Wrong scale for planned 1/10 V1; geometry reference only | https://www.printables.com/model/236070-scx24-low-cg-battery-tray-v1 |

## Custom CAD queue

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

## First prototype sequence

1. Select the rover chassis.
2. Measure the Pixhawk and inventory its bundled GPS/power hardware.
3. Lay the major rover components physically on the chassis.
4. CAD a simple electronics tray before attempting a fully sealed enclosure.
5. Print in inexpensive filament for fit checks.
6. Revise clearances and wire routing.
7. Move final wet-environment parts to a more appropriate filament.
