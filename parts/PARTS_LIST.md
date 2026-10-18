# Remote Car Master Parts List

Use this as the research checklist for the physical build.

Suggested status values:

- **Owned**
- **Researching**
- **Selected**
- **Ordered**
- **Received**
- **Installed**
- **Rejected**
- **Not needed**

---

## 1. Chassis and drivetrain

| Item | Requirement / target | Brand | Model | Qty | Budget | Actual price | Status | Notes |
|---|---|---|---|---:|---:|---:|---|---|
| 1/10 chassis | 4WD crawler or trail-truck style preferred | TBD | TBD | TBD | TBD | TBD | Researching | Must have room for Pixhawk enclosure |
| Chassis body / shell | Fits chassis and enclosure layout | TBD | TBD | TBD | TBD | TBD | Researching | Prefer easy access to electronics |
| 540/550 brushed motor | Approx. 27T-35T for V1 | TBD | TBD | TBD | TBD | TBD | Researching | Low-speed control prioritized |
| Pinion gear | Match motor shaft and drivetrain | TBD | TBD | TBD | TBD | TBD | Researching | Final tooth count depends on chassis |
| Spur gear | Compatible with chassis | TBD | TBD | TBD | TBD | TBD | Researching | May already be included |
| Motor mount | Compatible with selected chassis/motor | TBD | TBD | TBD | TBD | TBD | Researching | May already be included |
| Driveshafts | Appropriate for 4WD chassis | TBD | TBD | TBD | TBD | TBD | Researching | May already be included |
| Differentials / axles | Compatible with selected chassis | TBD | TBD | TBD | TBD | TBD | Researching | Usually included with donor chassis |
| Wheels | Terrain appropriate | TBD | TBD | TBD | TBD | TBD | Researching | |
| Tires | Trail / grass / light off-road | TBD | TBD | TBD | TBD | TBD | Researching | |
| Wheel hexes / adapters | Match chassis and wheels | TBD | TBD | TBD | TBD | TBD | Researching | If required |
| Bearings | Sealed preferred | TBD | TBD | TBD | TBD | TBD | Researching | Consider spares |
| Suspension parts | Shocks, springs, links as required | TBD | TBD | TBD | TBD | TBD | Researching | May be included |

---

## 2. Steering

| Item | Requirement / target | Brand | Model | Qty | Budget | Actual price | Status | Notes |
|---|---|---|---|---:|---:|---:|---|---|
| Steering servo | Waterproof, metal gear, approx. 20-30 kg-cm | TBD | TBD | TBD | TBD | TBD | Researching | Verify operating voltage |
| Servo horn | Metal preferred, correct spline | TBD | TBD | TBD | TBD | TBD | Researching | |
| Steering linkage | Zero binding through full travel | TBD | TBD | TBD | TBD | TBD | Researching | Usually chassis-specific |
| Servo saver | Protect servo/drivetrain | TBD | TBD | TBD | TBD | TBD | Researching | If not included |

---

## 3. Motor control and high-current power

| Item | Requirement / target | Brand | Model | Qty | Budget | Actual price | Status | Notes |
|---|---|---|---|---:|---:|---:|---|---|
| ESC | Waterproof brushed ESC, forward/brake/reverse | TBD | TBD | TBD | TBD | TBD | Researching | Must support selected battery/motor |
| ESC BEC | Adequate for steering servo if using built-in BEC | TBD | TBD | TBD | TBD | TBD | Researching | Check continuous and peak current |
| External BEC | 5-6 V regulated, high-current if required | TBD | TBD | TBD | TBD | TBD | Researching | Optional if ESC BEC is sufficient |
| Main fuse | Sized from real drivetrain current and wire limits | TBD | TBD | TBD | TBD | TBD | Researching | Blade-style holder is practical |
| Fuse holder | Low-resistance, accessible | TBD | TBD | TBD | TBD | TBD | Researching | |
| Master disconnect | Fast battery isolation | TBD | TBD | TBD | TBD | TBD | Researching | Connector may serve this function |
| Main battery connector | Polarized, adequate current rating | Assorted | XT60 / IC5 / EC5 | Assorted | $0 | TBD | Owned | Exact quantities and male/female combinations TBD |
| High-current wire | Silicone insulated, appropriately sized | TBD | TBD | TBD | TBD | TBD | Researching | Gauge based on current and length |
| Low-current wire | Sensors / signals / accessories | TBD | TBD | TBD | TBD | TBD | Researching | |

---

## 4. Battery and charging

| Item | Requirement / target | Brand | Model | Qty | Budget | Actual price | Status | Notes |
|---|---|---|---|---:|---:|---:|---|---|
| Main battery | 2S hardcase LiPo, around 5000 mAh target | TBD | TBD | TBD | TBD | TBD | Researching | Verify dimensions and connector |
| Spare battery | Same electrical specification if desired | TBD | TBD | TBD | TBD | TBD | Researching | Optional |
| Balance charger | Supports LiPo balance and storage charging | TBD | TBD | TBD | TBD | TBD | Researching | |
| Charger power supply | If charger does not include one | TBD | TBD | TBD | TBD | TBD | Researching | |
| LiPo storage bag / container | Charging and storage safety | TBD | TBD | TBD | TBD | TBD | Researching | |
| Battery voltage checker | Quick field verification | TBD | TBD | TBD | TBD | TBD | Researching | Optional but useful |

---

## 5. Flight controller and navigation

| Item | Requirement / target | Brand | Model | Qty | Budget | Actual price | Status | Notes |
|---|---|---|---|---:|---:|---:|---|---|
| Flight controller | Pixhawk 2.4.8 | TBD bundle brand | Pixhawk 2.4.8 | 1 | $0 | TBD | Owned | Part of owned drone-oriented bundle; validate board/sensors before use |
| Power module | Pixhawk-compatible and current-rated | TBD | TBD | TBD | TBD | TBD | Researching | Must support battery monitoring |
| GPS module | ArduPilot-compatible | TBD | TBD | TBD | TBD | TBD | Researching | |
| External compass | Prefer integrated with GPS module | TBD | TBD | TBD | TBD | TBD | Researching | Mount away from high-current wiring |
| Safety switch | Compatible with Pixhawk | TBD | TBD | TBD | TBD | TBD | Researching | May already be owned |
| Buzzer | Pixhawk-compatible | TBD | TBD | TBD | TBD | TBD | Researching | May already be owned |
| MicroSD card | Reliable card for ArduPilot logs | TBD | TBD | TBD | TBD | TBD | Researching | |
| Vibration isolation | Foam / gel / rubber mount | TBD | TBD | TBD | TBD | TBD | Researching | |

---

## 6. Radio control

| Item | Requirement / target | Brand | Model | Qty | Budget | Actual price | Status | Notes |
|---|---|---|---|---:|---:|---:|---|---|
| RC transmitter | Minimum 6 useful channels | TBD | TBD | TBD | TBD | TBD | Researching | Pistol or stick radio |
| RC receiver | Compatible with transmitter and Pixhawk | TBD | TBD | TBD | TBD | TBD | Researching | SBUS, PPM, or supported serial protocol |
| Receiver antennas | Correct for selected receiver | TBD | TBD | TBD | TBD | TBD | Researching | Usually included |
| Antenna mounts | Protect and orient antennas | TBD | TBD | TBD | TBD | TBD | Researching | |
| Channel switch hardware | Enough switches for modes/HOLD/arm | TBD | TBD | TBD | TBD | TBD | Researching | Usually part of transmitter |

---

## 7. Telemetry and data

| Item | Requirement / target | Brand | Model | Qty | Budget | Actual price | Status | Notes |
|---|---|---|---|---:|---:|---:|---|---|
| MAVLink telemetry radio | Optional for V1, useful for field tuning | TBD | TBD | TBD | TBD | TBD | Researching | Frequency must be legal for use |
| Ground telemetry adapter | Matches vehicle telemetry radio | TBD | TBD | TBD | TBD | TBD | Researching | |
| USB cable | Correct Pixhawk USB connector | TBD | TBD | TBD | TBD | TBD | Researching | |
| Laptop / ground station | Runs Mission Planner | Existing / TBD | Existing / TBD | 1 | TBD | TBD | Researching | |

---

## 8. Waterproof electronics enclosure

| Item | Requirement / target | Brand | Model | Qty | Budget | Actual price | Status | Notes |
|---|---|---|---|---:|---:|---:|---|---|
| Main electronics box | Gasketed polycarbonate preferred | TBD | TBD | TBD | TBD | TBD | Researching | Must fit Pixhawk and receiver |
| Cable glands | Sizes matched to actual cables | TBD | TBD | TBD | TBD | TBD | Researching | Prefer downward/side exits |
| Replacement gasket material | Closed-cell / suitable sealing material | TBD | TBD | TBD | TBD | TBD | Researching | Optional |
| Pressure equalization vent | Waterproof membrane vent | TBD | TBD | TBD | TBD | TBD | Researching | Optional |
| Desiccant packets | Small reusable or replaceable packs | TBD | TBD | TBD | TBD | TBD | Researching | |
| Moisture indicators | Paper/card indicators for testing | TBD | TBD | TBD | TBD | TBD | Researching | |
| Rubber isolation mounts | Electronics tray isolation | TBD | TBD | TBD | TBD | TBD | Researching | |
| Electronics tray material | 3D printed or sheet material | TBD | TBD | TBD | TBD | TBD | Researching | |

---

## 9. Waterproofing and electrical protection

| Item | Requirement / target | Brand | Model | Qty | Budget | Actual price | Status | Notes |
|---|---|---|---|---:|---:|---:|---|---|
| Marine heat-shrink | Adhesive-lined | TBD | TBD | TBD | TBD | TBD | Researching | |
| Standard heat-shrink | Assorted signal-wire sizes | TBD | Assorted | Assorted | $0 | TBD | Owned | Used with owned heat gun for solder-joint insulation |
| Dielectric grease | Connector protection | TBD | TBD | TBD | TBD | TBD | Researching | |
| Conformal coating | For selected exposed PCBs only | TBD | TBD | TBD | TBD | TBD | Researching | Avoid connectors/sensors |
| Silicone sealant | Electronics-safe type | TBD | TBD | TBD | TBD | TBD | Researching | |
| Liquid electrical tape | Optional supplemental sealing | TBD | TBD | TBD | TBD | TBD | Researching | |
| Self-fusing silicone tape | Field repair / cable protection | TBD | TBD | TBD | TBD | TBD | Researching | |

---

## 10. Connectors and wiring hardware

| Item | Requirement / target | Brand | Model | Qty | Budget | Actual price | Status | Notes |
|---|---|---|---|---:|---:|---:|---|---|
| Servo extension cables | Correct lengths and conductor size | TBD | TBD | TBD | TBD | TBD | Researching | |
| JST / DF13 / Pixhawk cables | As required by selected hardware | TBD | TBD | TBD | TBD | TBD | Researching | Verify exact connector standard |
| Heat-shrink labels | Wire identification | TBD | TBD | TBD | TBD | TBD | Researching | Optional |
| Crimp terminals | Match selected connectors | TBD | TBD | TBD | TBD | TBD | Researching | |
| Connector housings | Match terminals | TBD | TBD | TBD | TBD | TBD | Researching | |
| Cable sleeving | Abrasion protection | TBD | TBD | TBD | TBD | TBD | Researching | |
| Zip ties | UV-resistant preferred | TBD | TBD | TBD | TBD | TBD | Researching | |
| Adhesive cable mounts | For strain relief | TBD | TBD | TBD | TBD | TBD | Researching | |

---

## 11. Mechanical mounting hardware

| Item | Requirement / target | Brand | Model | Qty | Budget | Actual price | Status | Notes |
|---|---|---|---|---:|---:|---:|---|---|
| M2 hardware | Assorted lengths | TBD | TBD | TBD | TBD | TBD | Researching | |
| M2.5 hardware | Assorted lengths | TBD | TBD | TBD | TBD | TBD | Researching | |
| M3 hardware | Assorted lengths | TBD | TBD | TBD | TBD | TBD | Researching | |
| Lock nuts | Match selected fasteners | TBD | TBD | TBD | TBD | TBD | Researching | |
| Washers | Assorted | TBD | TBD | TBD | TBD | TBD | Researching | |
| Threadlocker | Removable / medium strength | TBD | TBD | TBD | TBD | TBD | Researching | Keep away from incompatible plastics |
| Rubber washers | Isolation / sealing | TBD | TBD | TBD | TBD | TBD | Researching | |
| Threaded inserts | For 3D-printed parts | TBD | TBD | TBD | TBD | TBD | Researching | Optional |

---

## 12. 3D printed parts and fabrication

| Item | Requirement / target | Brand | Model | Qty | Budget | Actual price | Status | Notes |
|---|---|---|---|---:|---:|---:|---|---|
| Electronics tray | Custom to enclosure/Pixhawk | N/A | Custom | TBD | TBD | TBD | Researching | Ender 3 V2 compatible design |
| GPS mast | Raise and isolate GPS/compass | N/A | Custom | TBD | TBD | TBD | Researching | Avoid metal directly over antenna |
| Antenna mount | Protect receiver antennas | N/A | Custom | TBD | TBD | TBD | Researching | |
| Cable gland support | If enclosure wall needs reinforcement | N/A | Custom | TBD | TBD | TBD | Researching | |
| Bumper / sensor mount | Optional later | N/A | Custom | TBD | TBD | TBD | Researching | |
| Filament | PETG/ASA preferred over PLA for outdoor heat/water | Assorted | Assorted filament | Assorted | $0 | TBD | Owned | Large existing filament supply; exact materials/quantities TBD |

---

## 13. Tools and test equipment

| Item | Requirement / target | Brand | Model | Qty | Budget | Actual price | Status | Notes |
|---|---|---|---|---:|---:|---:|---|---|
| Digital multimeter | Voltage, resistance, continuity | TBD | TBD | 1 | $0 | TBD | Owned | |
| Soldering iron | Temperature controlled | TBD | TBD | 1 | $0 | TBD | Owned | Soldering setup includes stand/helping hands and magnifier |
| Solder | Electronics appropriate | TBD | TBD | Assorted | $0 | TBD | Owned | |
| Flux | Electronics appropriate | TBD | Rosin paste | 1+ | $0 | TBD | Owned | Tip tinner also owned |
| Wire stripper | Covers selected wire gauges | TBD | TBD | 1 | $0 | TBD | Owned | |
| Crimping tool | Matches selected terminals | TBD | TBD | TBD | TBD | TBD | Researching | |
| Heat gun | For adhesive heat-shrink | TBD | TBD | 1 | $0 | TBD | Owned | |
| Hex drivers | Match RC chassis hardware | TBD | TBD | TBD | TBD | TBD | Researching | |
| Small screwdrivers | Electronics and chassis work | Assorted | Assorted | Assorted | $0 | TBD | Owned | Wrenches also owned |
| Calipers | Measure mounting and enclosure geometry | TBD | TBD | 1 | $0 | TBD | Owned | |
| Infrared thermometer | Motor/ESC temperature checks | TBD | TBD | TBD | TBD | TBD | Researching | Optional |
| Current meter / watt meter | Verify drivetrain current | TBD | TBD | TBD | TBD | TBD | Researching | Strongly useful before fuse selection |
| Portable fog machine | Airflow/smoke visualization for mini wind-tunnel experiments | COLBOR | Portable fog machine (exact model TBD) | 1 | $0 | TBD | Owned | Supporting test equipment; not required for rover V1 |

---

## 14. Optional later upgrades

| Item | Requirement / target | Brand | Model | Qty | Budget | Actual price | Status | Notes |
|---|---|---|---|---:|---:|---:|---|---|
| Front lidar / rangefinder | ArduPilot-compatible | TBD | TBD | TBD | TBD | TBD | Not needed | Post-V1 |
| Wheel encoders | Suitable resolution and mounting | TBD | TBD | TBD | TBD | TBD | Not needed | Post-V1 |
| Companion computer | Raspberry Pi / similar if required | Raspberry Pi | Raspberry Pi 4 Model B, 2 GB | 1 | $0 | TBD | Owned | Optional post-V1 companion computer |
| FPV camera | Waterproof/protected | TBD | TBD | TBD | TBD | TBD | Not needed | Post-V1 |
| Video transmitter | Compatible with camera/legal frequency | TBD | TBD | TBD | TBD | TBD | Not needed | Post-V1 |
| Headlights | Low-current LED | TBD | TBD | TBD | TBD | TBD | Not needed | |
| Tail / brake lights | Optional | TBD | TBD | TBD | TBD | TBD | Not needed | |
| Higher-performance drivetrain | Only after controls are proven | TBD | TBD | TBD | TBD | TBD | Not needed | Post-V1 |

---

# Research questions to resolve

Before final purchasing decisions, answer:

- What chassis are we building around?
- What motor current does that chassis/drivetrain actually draw?
- What ESC rating is appropriate with margin?
- Is the ESC BEC strong enough for the chosen servo?
- What exact servo voltage will we use?
- Which connector standard will be used across the high-current system?
- What Pixhawk power module is compatible with both voltage and peak current?
- What transmitter/receiver protocol will connect cleanly to the Pixhawk?
- What enclosure dimensions are required after laying out the Pixhawk, receiver, and wiring?
- Which items are already owned?
- Which items need spares?
- What parts should be bought locally versus online?


---

---

## 15. Owned inventory relevant to remote-car

These are owned parts that are directly useful to the rover or are shared workshop/electronics resources. Drone-specific propulsion hardware is tracked in `remote-drone`.

### Controllers, computers, cameras, and sensors

| Item | Brand | Model / specification | Qty | Status | Notes |
|---|---|---|---:|---|---|
| Pixhawk flight controller bundle | TBD | Pixhawk 2.4.8 bundle | 1 | Owned | Exact GPS, compass, power module, buzzer, safety switch, telemetry, and cables TBD |
| ESP32-CAM modules | Inland | ESP32-CAM Wi-Fi/Bluetooth camera modules | 2 | Owned | Optional camera/vision hardware |
| ESP32 Feather-format board | TBD | PAZO32 V2 Feather ESP32, 8 MB flash, 2 MB PSRAM, Wi-Fi/Bluetooth | 1 | Owned | Exact manufacturer/model spelling TBD |
| CMUcam5 Pixy | Charmed Labs / CMU-RI | Pixy Rev 2.3 (2021) | 1 | Owned | Includes stand and cables; optional vision sensor |
| M5Stack Timer Camera X | M5Stack | OV3660, Wi-Fi, BLE, UART, 8 MB PSRAM, 140 mAh battery, 66.5° FOV | 1 | Owned | Optional wireless vision module |
| Thermal IR module | TBD | AMG8831 or AMG8833 | 1 | Owned | Exact part number TBD |
| Raspberry Pi | Raspberry Pi | Raspberry Pi 4 Model B, 2 GB RAM | 1 | Owned | Optional companion computer |
| Bluetooth UART module | DSD TECH | 6-pin EN/VCC/GND/TXD/RXD/STATE module | 1 | Owned | Exact model TBD |
| Motor driver shield | TBD | L298P four-channel motor drive shield | 1 | Owned | For small auxiliary/bench motors, not rover traction motor |
| Micro servos | TBD | Basic micro servos | TBD | Owned | Auxiliary actuators only; not assumed suitable for steering |

### Wiring, passive electronics, and prototyping

| Item | Brand | Model / specification | Qty | Status | Notes |
|---|---|---|---:|---|---|
| Power cables/connectors | Assorted | XT60 / IC5 / EC5 | Assorted | Owned | Exact quantities/genders/wire gauges TBD |
| Signal cables | TBD | Pre-crimped Dupont 2.54 mm to JST-SH 1.0 mm | Assorted | Owned | Verify pinout before use |
| Jumper wires/cables | Assorted | Assorted | Assorted | Owned | |
| PCB prototyping boards | Assorted | Prototyping/perf boards | Assorted | Owned | |
| Capacitors | TBD | 1000 µF | 20 | Owned | Voltage rating TBD |
| Resistors | Assorted | Assorted values | Assorted | Owned | |
| Breadboard | TBD | Standard prototyping breadboard | 1+ | Owned | |

### Fabrication, tools, and test equipment

| Item | Brand | Model / specification | Qty | Status | Notes |
|---|---|---|---:|---|---|
| 3D printer | Existing | Existing printer | 1 | Owned | Large filament supply also owned |
| 3D-printing filament | Assorted | Assorted materials/colors | Assorted | Owned | Exact materials/quantities TBD |
| Portable fog machine | COLBOR | Portable fog machine, exact model TBD | 1 | Owned | Airflow visualization / mini wind-tunnel experiments |
| Heat gun | TBD | TBD | 1 | Owned | |
| Heat-shrink tubing | Assorted | Assorted sizes | Assorted | Owned | |
| Digital multimeter | TBD | TBD | 1 | Owned | |
| Soldering setup | Assorted | Soldering iron + stand/helping hands + magnifier | 1 set | Owned | Includes solder, rosin paste/flux, and tip tinner |
| Calipers | TBD | TBD | 1 | Owned | |
| Wrenches | Assorted | Assorted | Assorted | Owned | |
| Screwdrivers | Assorted | Assorted | Assorted | Owned | |
| Wire strippers | TBD | TBD | 1 | Owned | |
| Super glue | TBD | Cyanoacrylate adhesive | 1+ | Owned | |
| Safety glasses | TBD | TBD | 1+ | Owned | |

### Car-side lookup checklist

- Pixhawk 2.4.8 bundle accessory models and ratings
- PAZO32 V2 exact manufacturer/product spelling
- DSD TECH Bluetooth UART exact model
- AMG8831 vs AMG8833
- micro servo model/quantity/specs
- 1000 µF capacitor voltage ratings
- Dupont-to-JST-SH conductor count and pinout
- XT60 / IC5 / EC5 quantities, genders, and wire gauges
