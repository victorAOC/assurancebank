from tkinter import *
from functools import partial
from tkinter import messagebox, simpledialog


class LoginWindow:
    def __init__(self, tk_window):
        self.tk_window = tk_window
        self.tk_window.geometry('400x150')
        self.tk_window.title("Login Form")

        self.canvas = Canvas(tk_window, width=700, height=450)
        self.canvas.pack()

        # Load the background image
        self.background_image = PhotoImage(file="money2.png")

        # Place the background image on the canvas
        self.canvas.create_image(0, 0, image=self.background_image, anchor="nw")

        # Account number label and text entry box
        self.account_number_label = Label(self.tk_window, text="Account number", bg='white')
        self.account_number_label.place(x=10, y=10)
        self.account_number = StringVar()
        self.account_number_entry = Entry(self.tk_window, textvariable=self.account_number)
        self.account_number_entry.place(x=150, y=10)

        # Pin label and password entry box
        self.pin_label = Label(self.tk_window, text="Pin", bg='white')
        self.pin_label.place(x=10, y=40)
        self.pin = StringVar()
        self.pin_entry = Entry(self.tk_window, textvariable=self.pin, show='*')
        self.pin_entry.place(x=150, y=40)

        self.validate_login = partial(self.validate_login, self.account_number, self.pin)

        # Login button
        self.login_button = Button(self.tk_window, text="Login", command=self.validate_login)
        self.login_button.place(x=10, y=70)

    def validate_login(self, account_number, pin):
        self.account_number = "1234567890"
        self.pin = "1234"
        entered_account_number = account_number.get()
        entered_pin = pin.get()

        print("Account number entered:", entered_account_number)
        print("Pin entered:", entered_pin)

        if entered_account_number == self.account_number and entered_pin == self.pin:
            self.open_bank_account_window()
        else:
            messagebox.showinfo("Invalid", "Invalid account number or pin. Please try again.")

    def open_bank_account_window(self):
        self.tk_window.withdraw()
        BankAccountWindow()


class BankAccountWindow(Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Bank Account")
        self.geometry("400x300")

        self.bank_account_label = Label(self, text="Select account type")
        self.bank_account_label.grid(row=0, column=0, padx=10, pady=10)

        self.savings_button = Button(self, text="Savings Account", command=self.open_savings_account_window)
        self.savings_button.grid(row=1, column=0, padx=10, pady=5)

        self.current_button = Button(self, text="Current Account", command=self.open_current_account_window)
        self.current_button.grid(row=2, column=0, padx=10, pady=5)

        self.exit_button = Button(self, text="Exit", command=self.destroy)
        self.exit_button.grid(row=4, column=1, padx=10, pady=5)

    def open_savings_account_window(self):
        self.withdraw()
        account_number = "1234567890"  # Replace with the actual account number
        savings_window = SavingsAccountWindow(account_number)
        savings_window.mainloop()

    def open_current_account_window(self):
        self.withdraw()
        account_number = "1234567890"  # Replace with the actual account number
        current_window = CurrentAccountWindow(account_number)
        current_window.mainloop()


class SavingsAccountWindow(Toplevel):
    def __init__(self, account_number, initial_balance=0, withdrawal_limit=15000):
        super().__init__()
        self.account_number = account_number
        self.balance = initial_balance
        self.withdrawal_limit = withdrawal_limit

        self.title("Savings Account")
        self.geometry("400x300")

        self.balance_label = Label(self, text="Balance: $0.00")
        self.balance_label.pack(pady=10)

        self.deposit_button = Button(self, text="Deposit", command=self.deposit)
        self.deposit_button.pack(pady=5)

        self.withdraw_button = Button(self, text="Withdraw", command=self.withdraw)
        self.withdraw_button.pack(pady=5)

        self.quit_button = Button(self, text="Quit", command=self.destroy)
        self.quit_button.pack(pady=10)

    def deposit(self):
        deposit_amount = float(simpledialog.askstring("Deposit", "Enter deposit amount:"))
        if deposit_amount > 0:
            self.balance += deposit_amount
            self.update_balance_label()

    def withdraw(self):
        withdraw_amount = float(simpledialog.askstring("Withdraw", "Enter withdrawal amount:"))
        if 0 < withdraw_amount <= self.balance and withdraw_amount <= self.withdrawal_limit:
            self.balance -= withdraw_amount
            self.update_balance_label()
        else:
            messagebox.showwarning("Invalid Withdrawal", "Invalid withdrawal amount or insufficient funds.")

    def update_balance_label(self):
        self.balance_label.config(text="Balance: ${:.2f}".format(self.balance))


class CurrentAccountWindow(Toplevel):
    def __init__(self, account_number, initial_balance=0, overdraft_limit=5000):
        super().__init__()
        self.account_number = account_number
        self.balance = initial_balance
        self.overdraft_limit = overdraft_limit

        self.title("Current Account")
        self.geometry("400x300")

        self.balance_label = Label(self, text="Balance: $0.00")
        self.balance_label.pack(pady=10)

        self.deposit_button = Button(self, text="Deposit", command=self.deposit)
        self.deposit_button.pack(pady=5)

        self.withdraw_button = Button(self, text="Withdraw", command=self.withdraw)
        self.withdraw_button.pack(pady=5)

        self.quit_button = Button(self, text="Quit", command=self.destroy)
        self.quit_button.pack(pady=10)

    def deposit(self):
        deposit_amount = float(simpledialog.askstring("Deposit", "Enter deposit amount:"))
        if deposit_amount > 0:
            self.balance += deposit_amount
            self.update_balance_label()

    def withdraw(self):
        withdraw_amount = float(simpledialog.askstring("Withdraw", "Enter withdrawal amount:"))
        if 0 < withdraw_amount <= self.balance + self.overdraft_limit:
            self.balance -= withdraw_amount
            self.update_balance_label()
        else:
            messagebox.showwarning("Invalid Withdrawal", "Invalid withdrawal amount or insufficient funds.")

    def update_balance_label(self):
        self.balance_label.config(text="Balance: ${:.2f}".format(self.balance))


root = Tk()
login_window = LoginWindow(root)
root.mainloop()
