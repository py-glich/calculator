from tkinter import *

class Calculator(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("350x400")
        self.title("Dark Calculator")
        self.configure(bg="black")  # Set window background to black

        self.entry_widget = Entry(self, font=("Arial", 21), bd=5, relief=RIDGE,
                                  justify="right", bg="black", fg="white", insertbackground="white")
        self.entry_widget.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="we")

        btn_style = {"font": ("Arial", 24), "bd": 5, "relief": RIDGE,
                     "bg": "black", "fg": "white", "activebackground": "gray", "activeforeground": "white"}

        Button(self, text='Clear', command=self.clear_all, **btn_style).grid(row=1, column=0)
        Button(self, text='⌫', command=self.remove, **btn_style).grid(row=1, column=1)
        Button(self, text='=', command=self.calculate_result, **btn_style).grid(row=1, column=2)

        # Numbers
        Button(self, text='7', command=lambda: self.add_to_entry('7'), **btn_style).grid(row=2, column=0)
        Button(self, text='8', command=lambda: self.add_to_entry('8'), **btn_style).grid(row=2, column=1)
        Button(self, text='9', command=lambda: self.add_to_entry('9'), **btn_style).grid(row=2, column=2)

        Button(self, text='4', command=lambda: self.add_to_entry('4'), **btn_style).grid(row=3, column=0)
        Button(self, text='5', command=lambda: self.add_to_entry('5'), **btn_style).grid(row=3, column=1)
        Button(self, text='6', command=lambda: self.add_to_entry('6'), **btn_style).grid(row=3, column=2)

        Button(self, text='1', command=lambda: self.add_to_entry('1'), **btn_style).grid(row=4, column=0)
        Button(self, text='2', command=lambda: self.add_to_entry('2'), **btn_style).grid(row=4, column=1)
        Button(self, text='3', command=lambda: self.add_to_entry('3'), **btn_style).grid(row=4, column=2)

        Button(self, text='+', command=self.addition, **btn_style).grid(row=5, column=0)
        Button(self, text='0', command=lambda: self.add_to_entry('0'), **btn_style).grid(row=5, column=1)
        Button(self, text='.', command=lambda: self.add_to_entry('.'), **btn_style).grid(row=5, column=2)


class Function(Calculator):
    def clear_all(self):
        self.entry_widget.delete(0, END)

    def remove(self):
        current = self.entry_widget.get()
        if current:
            self.entry_widget.delete(len(current) - 1, END)

    def calculate_result(self):
        try:
            expression = self.entry_widget.get()
            result = eval(expression)
            self.entry_widget.delete(0, END)
            self.entry_widget.insert(0, str(result))
        except Exception:
            self.entry_widget.delete(0, END)
            self.entry_widget.insert(0, "Error")

    def add_to_entry(self, value):
        self.entry_widget.insert(END, value)

    def addition(self):
        self.add_to_entry('+')


if __name__ == '__main__':
    window = Function()
    window.mainloop()


