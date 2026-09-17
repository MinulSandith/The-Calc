# The Calc

A simple desktop calculator built with Python's built-in **Tkinter** GUI toolkit. Beyond the standard four operations, it supports a few extra math utilities: square, square root, prime factors, and HCF (Highest Common Factor).

![Calculator](https://user-images.githubusercontent.com/106053448/169861230-1142493d-aee8-4529-add0-77a1aa2cadec.jpg)

## Features

- Basic arithmetic: addition (`+`), subtraction (`-`), multiplication (`*`), division (`/`)
- `square` — squares a single number
- `square root` — square root of a single number
- `factors` — lists all factors of a single number
- `HCF` — Highest Common Factor of two numbers
- `clear` — resets the display and current calculation

## Requirements

- Python 3
- Tkinter (bundled with most Python installations; on Debian/Ubuntu install it separately with `sudo apt install python3-tk`)

## Running

```bash
python3 "The Calc.py"
```

Click the number and operator buttons to build an expression, then press `=` to evaluate.

> **Note:** This project currently supports only a single operation per calculation (e.g. `5 + 3`, not `5 + 3 * 2`). Entering more than one operator will show a message saying only one operation is supported.

## Project structure

| File | Description |
|---|---|
| `The Calc.py` | Main application — Tkinter UI and calculator logic |
| `Calculator.ico` | Window icon used on Windows |

## Known limitations

- Only one operation is supported per calculation.
- `HCF` returns `0`/an error if the two numbers are equal or if either factor list can't produce a common factor.
- The window icon (`Calculator.ico`) only applies on Windows; other platforms skip it gracefully.

## Contributing

Issues and pull requests are welcome. If you spot a bug, feel free to open an issue describing the steps to reproduce it.
