import tkinter as tk
from tkinter import messagebox
import datetime

class SavingsAccount:
    def __init__(self, account_number, initial_balance=0, account_type, transaction_type, withdrawal_limit=15000):
        self.account_number = account_number
        self.account_type = account_type
        self.balance = initial_balance
        self.withdrawal_limit = withdrawal_limit
        self.transaction_type = transaction_type

    def deposit(self, amount):
        self.balance += amount
        transaction = (datetime.datetime.now(), "Deposit:", amount)
        self.transaction_type.append(transaction)
        print(messagebox.showinfo(f"Deposit of {amount} {self.account_type} was successful"))

    def withdraw(self, amount):
        if amount <= self.balance and amount <= self.withdrawal_limit:
            self.balance -= amount
            transaction = (datetime.datetime.now(),"Withdrawal:", amount)
            self.transaction_type.append(transaction)
            self.withdrawal_limit -= amount
            print(messagebox.showinfo(f"Your withdrawal of {amount} {self.account_type} was successful"))
            #messagebox.showinfo("Withdrawal successful", "You have successfully withdrawn.")

        else:
            if amount > self.withdrawal_limit:
                messagebox.showerror("Withdrawal Limit Exceeded", "You have exceeded the withdrawal limit.")
            else:
                messagebox.showerror("Insufficient Funds", "You have insufficient funds for the withdrawal.")

    def get_balance(self):
        messagebox.showinfo("Account Balance", f"Current balance: ${self.balance}")


class SavingsAccountApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Savings Account App")

        self.account = SavingsAccount("123456789", withdrawal_limit=15000)  # Withdrawal limit set to 15000

        self.balance_label = tk.Label(self, text="Balance: $0")
        self.balance_label.grid(row=0, column=0, padx=10, pady=10)

        self.deposit_entry = tk.Entry(self)
        self.deposit_entry.grid(row=1, column=0, padx=10, pady=5)

        deposit_button = tk.Button(self, text="Deposit", command=self.deposit)
        deposit_button.grid(row=2, column=0, padx=10, pady=5)

        self.withdraw_entry = tk.Entry(self)
        self.withdraw_entry.grid(row=3, column=0, padx=10, pady=5)

        withdraw_button = tk.Button(self, text="Withdraw", command=self.withdraw)
        withdraw_button.grid(row=4, column=0, padx=10, pady=5)

        balance_button = tk.Button(self, text="Check Balance", command=self.check_balance)
        balance_button.grid(row=5, column=0, padx=10, pady=5)

    def deposit(self):
        amount = float(self.deposit_entry.get())
        self.account.deposit(amount)
        self.deposit_entry.delete(0, tk.END)
        self.update_balance()

    def withdraw(self):
        amount = float(self.withdraw_entry.get())
        self.account.withdraw(amount)
        self.withdraw_entry.delete(0, tk.END)
        self.update_balance()

    def check_balance(self):
        self.account.get_balance()

    def update_balance(self):
        self.balance_label.config(text=f"Balance: ${self.account.balance}")

    def save
if __name__ == "__main__":
    app = SavingsAccountApp()
    app.mainloop()
