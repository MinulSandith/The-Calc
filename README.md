# The Calc

A simple desktop calculator built with Python's built-in **Tkinter** GUI toolkit, styled with a dark theme, a two-line display, and a colored operator column. Beyond the standard four operations, it supports a few extra math utilities: square, square root, prime factors, and HCF (Highest Common Factor).

> The screenshot below predates the current dark theme; run the app to see the current look.

![Calculator](https://user-images.githubusercontent.com/106053448/169861230-1142493d-aee8-4529-add0-77a1aa2cadec.jpg)

## Features

- Dark-themed UI: black two-line display (dim expression / bold result), dark digit pad, light operator column, and an orange `=` accent
- Basic arithmetic: addition (`+`), subtraction (`-`), multiplication (`*`), division (`/`), with support for **chained operations** and parentheses (e.g. `5+3*2`)
- Decimal numbers (`.` button)
- Backspace (`⌫` button) to correct the last character
- Keyboard input: type digits/operators, `Enter` to evaluate, `Backspace` to delete, `Escape` to clear
- `square` — squares a single number
- `square root` — square root of a single number (returns a complex result for negative input)
- `factors` — lists all factors of a single whole number (capped at 1,000,000 to keep the UI responsive)
- `HCF` — Highest Common Factor of two numbers, computed with `math.gcd`
- `clear` — resets the display and current calculation
- Pressing a digit after a result starts a new calculation; pressing an operator continues from the result

## Requirements

- Python 3
- Tkinter (bundled with most Python installations; on Debian/Ubuntu install it separately with `sudo apt install python3-tk`)

## Running

```bash
python3 "The Calc.py"
```

Click the number and operator buttons (or type on your keyboard) to build an expression, then press `=` or `Enter` to evaluate.

## Project structure

| File | Description |
|---|---|
| `The Calc.py` | Main application — Tkinter UI and calculator logic |
| `Calculator.ico` | Window icon used on Windows |

## Known limitations

- `square`, `square root`, `factors`, and `HCF` are still standalone operations — they can't be mixed into a larger arithmetic expression in the same calculation.
- `factors` and `HCF` require whole-number input; decimals are rejected with an error rather than silently truncated.
- `factors` rejects numbers above 1,000,000, since checking every divisor of a much larger number would freeze the UI (there's no background thread).
- The window icon (`Calculator.ico`) only applies on Windows; other platforms skip it gracefully.

## Contributing

Issues and pull requests are welcome. If you spot a bug, feel free to open an issue describing the steps to reproduce it.
