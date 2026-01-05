# Test Cases

## TC1 — Start motor
Given: ESTOP_OK=1, OVERLOAD_OK=1, STOP_OK=1, FAULT=0  
When: START pressed  
Then: MOTOR_CONTACTOR=1

## TC2 — Stop motor
Given: motor running  
When: STOP pressed (STOP_OK=0)  
Then: MOTOR_CONTACTOR=0

## TC3 — E‑Stop override
Given: motor running  
When: ESTOP pressed (ESTOP_OK=0)  
Then: MOTOR_CONTACTOR=0 immediately, FAULT=1, ALARM=1

## TC4 — Overload trip
Given: motor running  
When: OVERLOAD trips (OVERLOAD_OK=0)  
Then: MOTOR=0, FAULT=1, ALARM=1

## TC5 — Reset after fault
Given: fault latched  
When: ESTOP_OK=1, OVERLOAD_OK=1, RESET pressed  
Then: FAULT=0, ALARM=0

## TC6 — Prevent restart during fault
Given: FAULT=1  
When: START pressed  
Then: MOTOR remains OFF until fault cleared
