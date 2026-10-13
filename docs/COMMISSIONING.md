# Commissioning

## Before power

- wheels off ground or vehicle restrained
- transmitter on
- throttle neutral
- emergency HOLD switch assigned
- propulsive wheels clear
- battery charged and physically undamaged
- polarity checked
- fuse installed

## First powered checks

1. Connect Pixhawk by USB only.
2. Confirm controller orientation.
3. Confirm radio input directions.
4. Confirm steering output with reduced travel.
5. Confirm throttle signal while drivetrain cannot move.
6. Verify neutral.
7. Verify forward and reverse.
8. Verify RC loss enters the configured failsafe.
9. Verify emergency switch selects HOLD.
10. Verify battery voltage against a multimeter.

## First outdoor test

- large empty area
- manual mode only
- speed limited
- short straight lines first
- inspect logs after each run

## Autonomous gate

Do not attempt AUTO until:
- manual control is reliable
- HOLD is reliable
- GPS fix is stable
- compass heading is correct
- battery monitor is calibrated
- geofence is configured
- RC failsafe is proven
- steering direction and endpoints are correct
