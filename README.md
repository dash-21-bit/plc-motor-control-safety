# PLC Motor Control + Safety Interlocks (Simulated)

A beginner-to-pro portfolio project that demonstrates **industrial PLC-style control logic** with a safety mindset.

## What it shows recruiters
- Start/Stop motor latching logic
- Emergency Stop (E‑Stop) override
- Thermal overload trip
- Manual reset after fault
- Test cases + documentation
- (Pro) A Python-based logic simulator + automated tests + CI

## Repository layout
- `logic/` — I/O list, ladder-style logic description, test cases
- `diagrams/` — draw.io files (add your screenshots/exported PNGs here)
- `report/` — project report (copy/paste into Word/PDF)
- `src/` + `tests/` — (Pro) logic simulator with pytest + GitHub Actions CI

## How to use (Simple)
Read:
- `logic/io_mapping.md`
- `logic/ladder_logic.md`
- `logic/test_cases.md`

## How to run (Pro)
```bash
pip install -U pytest
pytest -q
```

## Evidence to add
- Export your draw.io diagrams to PNG and place them in `diagrams/exports/`
- Add a short screen recording link in `evidence/demo_video_link.txt`
