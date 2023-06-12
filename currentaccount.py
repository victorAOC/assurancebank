import tkinter as tk


class CurrentAccountApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Current Account")
        self.geometry("400x300")

        self.balance = 0.0

        self.balance_label = tk.Label(self, text="Balance: $0.00")
        self.balance_label.pack(pady=10)

        self.deposit_button = tk.Button(self, text="Deposit", command=self.deposit)
        self.deposit_button.pack(pady=5)

        self.withdraw_button = tk.Button(self, text="Withdraw", command=self.withdraw)
        self.withdraw_button.pack(pady=5)

        self.quit_button = tk.Button(self, text="Quit", command=self.quit)
        self.quit_button.pack(pady=10)

    def deposit(self):
        deposit_amount = float(tk.simpledialog.askstring("Deposit", "Enter deposit amount:"))
        if deposit_amount > 0:
            self.balance += deposit_amount
            self.update_balance_label()

    def withdraw(self):
        withdraw_amount = float(tk.simpledialog.askstring("Withdraw", "Enter withdrawal amount:"))
        if 0 < withdraw_amount <= self.balance:
            self.balance -= withdraw_amount
            self.update_balance_label()
        else:
            tk.messagebox.showwarning("Withdraw", "Invalid withdrawal amount!")

    def update_balance_label(self):
        self.balance_label.config(text="Balance: ${:.2f}".format(self.balance))


app = CurrentAccountApp()
app.mainloop()