
#MOMO/ATM SIMULATOR
# FUNCTIONS : DEPOSIT  WITHDRAWAL  CHECK_BALANCE

MoMo_PIN = 2025
balance = 1000

# print(int(input("Enter amount to be deposited"))) // not in 
print("   Menu      ")
print("1.Deposit")
print("2.Withdrawal")
print("3.Check Balance")
option = (int(input("Enter an option:  ")))

# try:
if option == 1:
        amount = int(input("Enter an amount to deposit: "))
        balance = balance + amount
        print(f"Available balance is {balance}cedis")

elif option == 2:
        amount  = int(input("Enter amount to withdraw:  "))

        if amount > balance:
            print("Insufficient or not enough balance ")
        elif amount <= balance:
            MM_PIN = int(input("Enter MM PIN to confirm: "))
            balance = balance - amount
            if MM_PIN == MoMo_PIN:
                    print(f"{amount}cedis successfully withdrawn ")
                    print(f"Balance: {balance}cedis ")
            else :
                print("Wrong/Incorrect PIN.. Try again")

elif option == 3:
        MOMO_PIN = int(input("Enter MoMo PIN: "))
        if MOMO_PIN == MoMo_PIN:
            print(f"Available balance is {balance}cedis ")
        else:
            print("Incorrect MoMo PIN....!")
# except ValueError:
#     print("Value Error! Enter values from 1 to 3")