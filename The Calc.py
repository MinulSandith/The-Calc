import cmath
import math
import re
import tkinter as tk

DIGITS = "0123456789"
ARITH_OPS = "+-*/"
SAFE_EXPR = re.compile(r"[0-9+\-*/(). ]+")


class CalcApp:
    def __init__(self, root):
        self.root = root
        self.root.title("The Calc")

        try:
            self.root.iconbitmap("./Calculator.ico")
        except tk.TclError:
            pass
        try:
            self.root.attributes("-toolwindow", True)
        except tk.TclError:
            pass

        self.entry = tk.Entry(root, borderwidth=9, width=60)
        self.entry.grid(row=0, column=1, columnspan=5)
        self.just_evaluated = False

        self._build_buttons()
        self.root.bind("<Key>", self._on_key)

    # -- low-level entry helpers ------------------------------------

    def insert_text(self, text):
        if self.just_evaluated:
            self.just_evaluated = False
            if text and (text[0] in DIGITS or text[0] == "."):
                self.entry.delete(0, tk.END)
        self.entry.insert(tk.INSERT, text)

    def insert_decimal(self):
        pos = self.entry.index(tk.INSERT)
        before = self.entry.get()[:pos]
        last_segment = re.split(r"[+\-*/() ]", before)[-1]
        if "." not in last_segment:
            self.insert_text(".")

    def backspace(self):
        self.just_evaluated = False
        pos = self.entry.index(tk.INSERT)
        if pos > 0:
            self.entry.delete(pos - 1)

    def clear(self):
        self.entry.delete(0, tk.END)
        self.just_evaluated = False

    # -- evaluation ---------------------------------------------------

    def evaluate(self):
        text = self.entry.get().strip()
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

        self.entry.delete(0, tk.END)
        self.entry.insert(0, str(result))
        self.just_evaluated = True

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
        root = self.root

        def digit_btn(d, row, col):
            tk.Button(
                root, text=d, width=10, command=lambda: self.insert_text(d)
            ).grid(row=row, column=col)

        for d, (row, col) in zip("789", [(1, 1), (1, 2), (1, 3)]):
            digit_btn(d, row, col)
        for d, (row, col) in zip("456", [(2, 1), (2, 2), (2, 3)]):
            digit_btn(d, row, col)
        for d, (row, col) in zip("123", [(3, 1), (3, 2), (3, 3)]):
            digit_btn(d, row, col)
        digit_btn("0", 4, 2)

        def op_btn(text, op, row, col):
            tk.Button(
                root, text=text, width=10, command=lambda: self.insert_text(op)
            ).grid(row=row, column=col)

        op_btn("+", "+", 1, 4)
        op_btn("-", "-", 2, 4)
        op_btn("*", "*", 3, 4)
        op_btn("/", "/", 4, 4)

        tk.Button(root, text="clear", width=10, command=self.clear).grid(
            row=4, column=1
        )
        tk.Button(root, text="=", width=10, command=self.evaluate).grid(
            row=4, column=3
        )

        tk.Button(
            root, text="square", width=10, command=lambda: self.insert_text(" square ")
        ).grid(row=1, column=5)
        tk.Button(
            root,
            text="Square root",
            width=10,
            command=lambda: self.insert_text(" square root "),
        ).grid(row=2, column=5)
        tk.Button(
            root, text="Factors", width=10, command=lambda: self.insert_text(" factors ")
        ).grid(row=3, column=5)
        tk.Button(
            root, text="HCF", width=10, command=lambda: self.insert_text(" HCF ")
        ).grid(row=4, column=5)

        tk.Button(root, text="⌫", width=10, command=self.backspace).grid(
            row=5, column=1
        )
        tk.Button(root, text=".", width=10, command=self.insert_decimal).grid(
            row=5, column=2
        )


if __name__ == "__main__":
    root = tk.Tk()
    CalcApp(root)
    root.mainloop()
