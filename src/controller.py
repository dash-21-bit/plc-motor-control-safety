from dataclasses import dataclass

@dataclass
class Inputs:
    start: bool
    stop_ok: bool
    estop_ok: bool
    overload_ok: bool
    reset: bool

@dataclass
class Outputs:
    motor: bool
    alarm: bool

class PLCController:
    """Simulates PLC-style latching logic for motor control with a fault latch."""

    def __init__(self) -> None:
        self.motor_latch = False
        self.fault_latch = False

    def step(self, i: Inputs) -> Outputs:
        # Safety chain broken => fault + motor off
        if (not i.estop_ok) or (not i.overload_ok):
            self.fault_latch = True
            self.motor_latch = False

        # Reset fault only if safety chain is healthy
        if i.reset and i.estop_ok and i.overload_ok:
            self.fault_latch = False

        # Stop button always stops motor (break latch)
        if not i.stop_ok:
            self.motor_latch = False

        # Start allowed only if permissives OK and no fault
        permissive = i.stop_ok and i.estop_ok and i.overload_ok and (not self.fault_latch)
        if permissive and i.start:
            self.motor_latch = True

        return Outputs(motor=self.motor_latch, alarm=self.fault_latch)
