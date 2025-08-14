import tkinter as tk

### step 1
#create the main window
app = tk.Tk() 
app.title("Account Management System") #Window tittle
app.geometry("400x300") #Width x Height


###step 2
#label
label = tk.Label(app, text="Enter your PIN")
label.pack(pady=10)

#Entry for PIN input
# pin_entry = 

#Run the App
app.mainloop()

