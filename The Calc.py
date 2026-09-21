import cmath
import math
import re
import tkinter as tk
from tkinter import font as tkfont

DIGITS = "0123456789"
ARITH_OPS = "+-*/"
SAFE_EXPR = re.compile(r"[0-9+\-*/(). ]+")

# -- theme -----------------------------------------------------------------

BG_APP = "#0d0d0d"
BG_DISPLAY = "#000000"
BG_DIGIT = "#1c1c1e"
BG_DIGIT_ACTIVE = "#2c2c2e"
BG_FUNC = "#161616"
BG_FUNC_ACTIVE = "#232323"
BG_OP = "#f5f5f5"
BG_OP_ACTIVE = "#e2e2e2"
BG_EQUAL = "#ff6a00"
BG_EQUAL_ACTIVE = "#ff8534"

FG_DIGIT = "#ffffff"
FG_OP = "#1c1c1e"
FG_EQUAL = "#ffffff"
FG_FUNC = "#9a9a9a"
FG_DIM = "#7d7d7d"
FG_RESULT = "#ffffff"


def make_button(parent, text, bg, fg, active_bg, command, font):
    btn = tk.Button(
        parent,
        text=text,
        command=command,
        bg=bg,
        fg=fg,
        activebackground=active_bg,
        activeforeground=fg,
        font=font,
        relief="flat",
        borderwidth=0,
        highlightthickness=0,
        cursor="hand2",
    )
    return btn


class CalcApp:
    def __init__(self, root):
        self.root = root
        self.root.title("The Calc")
        self.root.configure(bg=BG_APP)
        self.root.minsize(320, 480)

        try:
            self.root.iconbitmap("./Calculator.ico")
        except tk.TclError:
            pass
        try:
            self.root.attributes("-toolwindow", True)
        except tk.TclError:
            pass

        self.buffer = ""
        self.history = ""
        self.just_evaluated = False

        self.digit_font = tkfont.Font(family="Helvetica", size=20, weight="bold")
        self.func_font = tkfont.Font(family="Helvetica", size=12)
        self.op_font = tkfont.Font(family="Helvetica", size=22)
        self.equal_font = tkfont.Font(family="Helvetica", size=22, weight="bold")
        self.history_font = tkfont.Font(family="Helvetica", size=16)
        self.result_font = tkfont.Font(family="Helvetica", size=38, weight="bold")

        self._build_header()
        self._build_display()
        self._build_buttons()
        self.root.bind("<Key>", self._on_key)

    # -- chrome ----------------------------------------------------------

    def _build_header(self):
        header = tk.Frame(self.root, bg=BG_APP, height=34)
        header.pack(fill="x", side="top")
        dots = tk.Canvas(
            header, width=60, height=34, bg=BG_APP, highlightthickness=0
        )
        dots.pack(side="left", padx=12)
        for i, color in enumerate(("#ff5f57", "#febc2e", "#28c840")):
            x = 6 + i * 18
            dots.create_oval(x, 13, x + 10, 23, fill=color, outline="")

        back = make_button(
            header, "⌫", BG_APP, FG_DIM, BG_APP, self.backspace, self.func_font
        )
        back.configure(relief="flat")
        back.pack(side="right", padx=10)

    def _build_display(self):
        display = tk.Frame(self.root, bg=BG_DISPLAY, height=140)
        display.pack(fill="x", side="top")
        display.pack_propagate(False)

        self.history_label = tk.Label(
            display,
            text="",
            bg=BG_DISPLAY,
            fg=FG_DIM,
            font=self.history_font,
            anchor="e",
            justify="right",
        )
        self.history_label.pack(fill="x", padx=20, pady=(18, 0))

        self.result_label = tk.Label(
            display,
            text="0",
            bg=BG_DISPLAY,
            fg=FG_RESULT,
            font=self.result_font,
            anchor="e",
            justify="right",
        )
        self.result_label.pack(fill="x", padx=20, pady=(0, 20))

    def _refresh_display(self):
        self.history_label.configure(text=self.history)
        self.result_label.configure(text=self.buffer if self.buffer else "0")

    # -- low-level buffer helpers -----------------------------------------

    def insert_text(self, text):
        if self.just_evaluated:
            self.just_evaluated = False
            if text and (text[0] in DIGITS or text[0] == "."):
                self.buffer = ""
            self.history = ""
        self.buffer += text
        self._refresh_display()

    def insert_decimal(self):
        last_segment = re.split(r"[+\-*/() ]", self.buffer)[-1]
        if "." not in last_segment:
            self.insert_text(".")

    def backspace(self):
        self.just_evaluated = False
        self.buffer = self.buffer[:-1]
        self._refresh_display()

    def clear(self):
        self.buffer = ""
        self.history = ""
        self.just_evaluated = False
        self._refresh_display()

    # -- evaluation ---------------------------------------------------

    def evaluate(self):
        text = self.buffer.strip()
        if not text:
            return

        try:
            if "square root" in text:
                num = float(text.replace("square root", "").strip())
                result = num**0.5 if num >= 0 else cmath.sqrt(num)
            elif "square" in text:
                num = float(text.replace("square", "").strip())
                result = num**2
            elif "factors" in text:
                num = int(float(text.replace("factors", "").strip()))
                if num <= 0:
                    raise ValueError("factors needs a positive integer")
                result = [d for d in range(1, num + 1) if num % d == 0]
            elif "HCF" in text:
                left, right = text.split("HCF")
                a = int(float(left.strip()))
                b = int(float(right.strip()))
                result = math.gcd(a, b)
            else:
                if not SAFE_EXPR.fullmatch(text):
                    raise ValueError("invalid characters")
                result = eval(text, {"__builtins__": {}}, {})
                if isinstance(result, float) and result.is_integer():
                    result = int(result)
        except ZeroDivisionError:
            result = "undefined"
        except Exception:
            result = "error"

        self.history = f"{text} ="
        self.buffer = str(result)
        self.just_evaluated = True
        self._refresh_display()

    # -- keyboard support ----------------------------------------------

    def _on_key(self, event):
        if event.char and event.char in DIGITS + ARITH_OPS:
            self.insert_text(event.char)
        elif event.char == ".":
            self.insert_decimal()
        elif event.keysym in ("Return", "KP_Enter"):
            self.evaluate()
        elif event.keysym == "BackSpace":
            self.backspace()
        elif event.keysym == "Escape":
            self.clear()

    # -- button layout --------------------------------------------------

    def _build_buttons(self):
        grid = tk.Frame(self.root, bg=BG_APP)
        grid.pack(fill="both", expand=True, side="bottom")
        for col in range(4):
            grid.columnconfigure(col, weight=1, uniform="col")
        for row in range(5):
            grid.rowconfigure(row, weight=1)

        def place(widget, row, col):
            widget.grid(row=row, column=col, sticky="nsew", padx=1, pady=1)

        # row 0: secondary math functions
        func_specs = [
            (" square root ", "√"),
            (" square ", "x²"),
            (" factors ", "Factors"),
            (" HCF ", "HCF"),
        ]
        for col, (token, label) in enumerate(func_specs):
            btn = make_button(
                grid,
                label,
                BG_FUNC,
                FG_FUNC,
                BG_FUNC_ACTIVE,
                lambda t=token: self.insert_text(t),
                self.func_font,
            )
            place(btn, 0, col)

        # rows 1-3: digit pad + operators
        digit_rows = [("7", "8", "9"), ("4", "5", "6"), ("1", "2", "3")]
        op_rows = [("÷", "/"), ("−", "-"), ("+", "+")]
        for r, (digits, (op_label, op_val)) in enumerate(zip(digit_rows, op_rows), start=1):
            for c, d in enumerate(digits):
                btn = make_button(
                    grid,
                    d,
                    BG_DIGIT,
                    FG_DIGIT,
                    BG_DIGIT_ACTIVE,
                    lambda d=d: self.insert_text(d),
                    self.digit_font,
                )
                place(btn, r, c)
            op_btn = make_button(
                grid,
                op_label,
                BG_OP,
                FG_OP,
                BG_OP_ACTIVE,
                lambda v=op_val: self.insert_text(v),
                self.op_font,
            )
            place(op_btn, r, 3)

        # row 4: clear, 0, decimal, equal
        clear_btn = make_button(
            grid, "AC", BG_DIGIT, FG_FUNC, BG_DIGIT_ACTIVE, self.clear, self.func_font
        )
        place(clear_btn, 4, 0)

        zero_btn = make_button(
            grid,
            "0",
            BG_DIGIT,
            FG_DIGIT,
            BG_DIGIT_ACTIVE,
            lambda: self.insert_text("0"),
            self.digit_font,
        )
        place(zero_btn, 4, 1)

        decimal_btn = make_button(
            grid,
            ",",
            BG_DIGIT,
            FG_DIGIT,
            BG_DIGIT_ACTIVE,
            self.insert_decimal,
            self.digit_font,
        )
        place(decimal_btn, 4, 2)

        equal_btn = make_button(
            grid, "=", BG_EQUAL, FG_EQUAL, BG_EQUAL_ACTIVE, self.evaluate, self.equal_font
        )
        place(equal_btn, 4, 3)


if __name__ == "__main__":
    root = tk.Tk()
    CalcApp(root)
    root.mainloop()
