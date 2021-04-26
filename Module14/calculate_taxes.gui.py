
import tkinter as tk
from calculate_taxes import *

class TaxUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculate Tax")
        self.geometry('150x150')
        self.label = tk.Label(self, text='Income')
        self.label.pack()
        self.income = tk.Entry (self)
        self.income.pack()
        self.button = tk.Button(self, text='Get My Tax')
        self.button['command'] = self.get_tax
        self.button.pack()
        self.label_tax = tk.Label(self, text='')
        

    def get_tax(self):
        income = self.income.get()
        taxObject = calculate_taxes()
        tax = taxObject.calculate_single_tax(int(income))
        self.label_tax = tk.Label(self, text=f'The Tax is : $ {tax}')
        self.label_tax.pack()


if __name__ == "__main__":
    app = TaxUI()
    app.mainloop()