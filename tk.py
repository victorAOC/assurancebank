from tkinter import *
from functools import partial


def validateLogin(accountnumber, pin):
    print("Account number entered :", accountnumber.get())
    print("Pin entered :", pin.get())
    return


# window
tkWindow = Tk()
tkWindow.geometry('400x150')
tkWindow.title('Tkinter Login Form - pythonexamples.org')

# account number label and text entry box
accountnumberLabel = Label(tkWindow, text="Account number").grid(row=0, column=0)
accountnumber = StringVar()
accountnumberEntry = Entry(tkWindow, textvariable=accountnumber).grid(row=0, column=1)

# pin label and password entry box
pinLabel = Label(tkWindow, text="Pin").grid(row=1, column=0)
pin = StringVar()
pinEntry = Entry(tkWindow, textvariable=pin, show='*').grid(row=1, column=1)

validateLogin = partial(validateLogin, accountnumber, pin)

# login button
loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=4, column=0)

tkWindow.mainloop()

if (accountnumber == 5172839405):
    if (pin == 1234):
        print("Welcome!!")

    else:
        print("Invalid pin try again")
        if (accountnumber == 5172839405):
            if (pin == 1234):
                print("Welcome!!")

        else:
            print("Invalid pin try again")