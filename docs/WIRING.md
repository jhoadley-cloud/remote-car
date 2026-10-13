# Wiring

## High-level power path

```text
2S LiPo
  |
main fuse
  |
current-rated Pixhawk power module
  |------------------> ESC ------------------> motor
  |
  +---- low-voltage power lead -------------> Pixhawk POWER
```

## Control

```text
RC receiver -------------------------------> Pixhawk RC IN / serial
GPS/compass -------------------------------> Pixhawk GPS + compass interface

Pixhawk MAIN OUT 1 ------------------------> steering servo signal
Pixhawk MAIN OUT 3 ------------------------> ESC signal
```

## Servo rail

Do not treat the Pixhawk as the steering servo power supply.

Use either:
- a sufficiently rated ESC BEC, or
- a dedicated regulated BEC

Keep signal ground common between Pixhawk, ESC, and servo supply.

## Physical placement

- Pixhawk near chassis center
- arrow forward
- vibration-isolated
- GPS antenna upward
- compass away from motor, ESC, battery leads, and other high-current wiring
- battery low and centered
- electronics enclosure above likely splash level

## Fuse sizing

Choose the fuse from known or measured drivetrain current and wire ratings. Do not exceed connector, wire, ESC, or power-module ratings.
