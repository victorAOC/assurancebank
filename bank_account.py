import tkinter as tk
from tkinter import messagebox, simpledialog


class BankAccount:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            messagebox.showwarning("Withdraw", "Invalid withdrawal amount!")

    def transfer(self, amount, target_account):
        if 0 < amount <= self.balance:
            self.balance -= amount
            target_account.balance += amount
        else:
            messagebox.showwarning("Transfer", "Invalid transfer amount!")


class BankApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Bank Account")
        self.geometry("400x300")

        self.current_account = BankAccount()
        self.savings_account = BankAccount()

        self.current_balance_label = tk.Label(self, text="Current Account Balance: $0.00")
        self.current_balance_label.pack(pady=10)

        self.savings_balance_label = tk.Label(self, text="Savings Account Balance: $0.00")
        self.savings_balance_label.pack(pady=10)

        self.deposit_button = tk.Button(self, text="Deposit", command=self.deposit)
        self.deposit_button.pack(pady=5)

        self.withdraw_button = tk.Button(self, text="Withdraw", command=self.withdraw)
        self.withdraw_button.pack(pady=5)

        self.transfer_button = tk.Button(self, text="Transfer", command=self.transfer)
        self.transfer_button.pack(pady=5)

        self.quit_button = tk.Button(self, text="Quit", command=self.quit)
        self.quit_button.pack(pady=10)

    def deposit(self):
        amount = float(simpledialog.askstring("Deposit", "Enter deposit amount:"))
        if amount > 0:
            if self.current_account_selected():
                self.current_account.deposit(amount)
            else:
                self.savings_account.deposit(amount)
            self.update_balance_labels()

    def withdraw(self):
        amount = float(simpledialog.askstring("Withdraw", "Enter withdrawal amount:"))
        if amount > 0:
            if self.current_account_selected():
                self.current_account.withdraw(amount)
            else:
                self.savings_account.withdraw(amount)
            self.update_balance_labels()

    def transfer(self):
        amount = float(simpledialog.askstring("Transfer", "Enter transfer amount:"))
        if amount > 0:
            if self.current_account_selected():
                self.current_account.transfer(amount, self.savings_account)
            else:
                self.savings_account.transfer(amount, self.current_account)
            self.update_balance_labels()

    def current_account_selected(self):
        return True  # Modify this function based on your UI design

    def update_balance_labels(self):
        self.current_balance_label.config(text="Current Account Balance: ${:.2f}".format(self.current_account.balance))
        self.savings_balance_label.config(text="Savings Account Balance: ${:.2f}".format(self.savings_account.balance))


app = BankApp()
app.mainloop()
