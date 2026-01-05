# Ladder Logic (Concept / Pseudocode)

This is written in ladder-style thinking so you can recreate it in any PLC environment.

## Rung 1 — Fault latch
**Set FAULT_LATCH** if the safety chain breaks:
- If NOT ESTOP_OK OR NOT OVERLOAD_OK  => FAULT_LATCH := TRUE
- FAULT_LATCH stays TRUE until RESET is pressed **AND** safety chain is healthy

**Reset FAULT_LATCH**
- If RESET_PB AND ESTOP_OK AND OVERLOAD_OK => FAULT_LATCH := FALSE

## Rung 2 — Motor latch (start/stop)
Motor may latch ON only if:
- STOP_PB is OK (NC contact closed)
- ESTOP_OK TRUE
- OVERLOAD_OK TRUE
- FAULT_LATCH FALSE

Start:
- If START_PB AND all permissives => MOTOR_LATCH := TRUE

Stop:
- If STOP_PB opens => MOTOR_LATCH := FALSE

Safety overrides:
- If FAULT_LATCH TRUE => MOTOR_LATCH := FALSE

## Rung 3 — Outputs
- MOTOR_CONTACTOR := MOTOR_LATCH
- ALARM_LAMP := FAULT_LATCH
