# Project Report — PLC Motor Control + Safety Interlocks (Simulated)

## 1) Objective
Design and validate a standard industrial motor control routine including Start/Stop latching and safety interlocks (E‑Stop + overload), with a manual reset requirement after fault.

## 2) Tools / Apps Used
- draw.io (or any diagram tool) for ladder/state diagrams
- Git + GitHub for version control and evidence
- (Pro) Python + pytest for logic simulation tests
- (Optional) PLC simulator / ladder editor if available

## 3) Requirements
- Motor shall start only when safety chain is healthy and Stop circuit is OK.
- E‑Stop shall override all logic and stop motor immediately.
- Overload shall stop motor and latch a fault.
- Fault shall require manual reset **and** healthy safety chain before allowing restart.

## 4) Design
- I/O list defined in `logic/io_mapping.md`
- Ladder-style logic defined in `logic/ladder_logic.md`
- Test cases in `logic/test_cases.md`

## 5) Implementation
Implemented as documentation + (Pro) executable simulation model:
- Fault latch behavior
- Motor latch behavior
- Output mapping

## 6) Testing
Executed TC1–TC6. For the Pro version, tests are implemented in `tests/test_controller.py`.

## 7) Results
Logic meets expected industrial behavior; safety chain overrides motor state; fault requires reset before restart.

## 8) Future Enhancements
- Add guard interlock input and safety relay modeling
- Add motor run feedback and start timeout fault
- Add maintenance mode / jog function with extra safeguards
