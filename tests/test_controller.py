from src.controller import PLCController, Inputs

def test_start_stop():
    plc = PLCController()

    out = plc.step(Inputs(start=True, stop_ok=True, estop_ok=True, overload_ok=True, reset=False))
    assert out.motor is True
    assert out.alarm is False

    out = plc.step(Inputs(start=False, stop_ok=False, estop_ok=True, overload_ok=True, reset=False))
    assert out.motor is False

def test_estop_override_and_reset():
    plc = PLCController()
    plc.step(Inputs(start=True, stop_ok=True, estop_ok=True, overload_ok=True, reset=False))

    out = plc.step(Inputs(start=False, stop_ok=True, estop_ok=False, overload_ok=True, reset=False))
    assert out.motor is False
    assert out.alarm is True

    # reset should not clear until estop restored
    out = plc.step(Inputs(start=False, stop_ok=True, estop_ok=False, overload_ok=True, reset=True))
    assert out.alarm is True

    out = plc.step(Inputs(start=False, stop_ok=True, estop_ok=True, overload_ok=True, reset=True))
    assert out.alarm is False
