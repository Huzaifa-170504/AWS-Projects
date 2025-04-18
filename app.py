import tkinter as tk
from math import *

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.geometry("400x600")
        self.expression = ""

        self.input_text = tk.StringVar()

        input_frame = tk.Frame(self.root, height=50, bg="lightgrey")
        input_frame.pack(side=tk.TOP, fill="both")

        input_field = tk.Entry(input_frame, font=('arial', 20, 'bold'), textvariable=self.input_text, bd=10, insertwidth=2, width=14, borderwidth=4, relief='ridge', justify='right')
        input_field.grid(row=0, column=0)
        input_field.pack(ipady=10)

        btns_frame = tk.Frame(self.root)
        btns_frame.pack()

        buttons = [
            ('C', '√', 'x²', '/'),
            ('7', '8', '9', '*'),
            ('4', '5', '6', '-'),
            ('1', '2', '3', '+'),
            ('0', '.', '(', ')'),
            ('sin', 'cos', 'tan', 'log'),
            ('ln', 'exp', 'π', 'e'),
            ('^', '=', '', '')
        ]

        for row_index, row in enumerate(buttons):
            for col_index, button_text in enumerate(row):
                if button_text:
                    btn = tk.Button(btns_frame, text=button_text, width=9, height=2, font=('arial', 12), bd=1, relief='ridge',
                                    command=lambda btn=button_text: self.click(btn))
                    btn.grid(row=row_index, column=col_index, padx=1, pady=1)

    def click(self, item):
        if item == 'C':
            self.expression = ""
            self.input_text.set("")
        elif item == '=':
            try:
                result = self.safe_eval(self.expression)
                self.input_text.set(result)
                self.expression = str(result)
            except Exception as e:
                self.input_text.set("Error")
                self.expression = ""
        elif item == '√':
            self.expression += "sqrt("
            self.input_text.set(self.expression)
        elif item == 'x²':
            self.expression += "**2"
            self.input_text.set(self.expression)
        elif item == '^':
            self.expression += "**"
            self.input_text.set(self.expression)
        elif item == 'π':
            self.expression += str(pi)
            self.input_text.set(self.expression)
        elif item == 'e':
            self.expression += str(e)
            self.input_text.set(self.expression)
        elif item in ['sin', 'cos', 'tan', 'log', 'ln', 'exp']:
            if item == 'ln':
                self.expression += "log("
            else:
                self.expression += item + "("
            self.input_text.set(self.expression)
        else:
            self.expression += str(item)
            self.input_text.set(self.expression)

    def safe_eval(self, expr):
        return eval(expr, {"__builtins__": None}, {
            "sin": sin, "cos": cos, "tan": tan, "sqrt": sqrt,
            "log": log10, "log10": log10, "log2": lambda x: log(x, 2),
            "exp": exp, "pi": pi, "e": e, "pow": pow
        })

if __name__ == "__main__":
    root = tk.Tk()
    calc = ScientificCalculator(root)
    root.mainloop()
