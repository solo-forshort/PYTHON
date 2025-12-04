from EncBankGroup import AccountSecured
import tkinter as tk
from tkinter import messagebox

### step 1
#create the main window
app = tk.Tk() 
app.title("Account Management System") #Window tittle
app.geometry("400x300") #Width x Height


###step 2
#label
label = tk.Label(app, text="Enter your PIN")
label.pack(pady=10)

pin_entry = tk.Entry(app, show="*")
pin_entry.pack(pady=5)

def check_balance():
    pin = pin_entry.get()
    if pin == "1234":  # temporary test PIN
        messagebox.showinfo("Balance", "Your balance is $500")
    else:
        messagebox.showerror("Error", "Incorrect PIN")

check_btn = tk.Button(app, text="Check Balance", command=check_balance)
check_btn.pack(pady=10)

#Run the App
app.mainloop()

