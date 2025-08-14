
from EncBankGroup import AccountSecured

def main():
    account = AccountSecured("123456", 5000)


    while True:
        print("\n  MENU")
        print("1. Check Balance. ")
        print("2. Change user Pin. ")
        print("3. check masked info")
        print("4. Exit")

        try:
            option = int(input("Enter an option[from 1 to 4]: \n"))
        except ValueError:
            print("Invalid option entered.")
            continue


        if option == 1:
            account.balance_checker()
        elif option == 2:
            account.change_USER_PIN()
        elif option == 3:
            account.acount_masking()
        elif option == 4:
            print("Exiting...")
            break
        else:
            print("Invalid Input. choose from 1 to 4")
    
if __name__ == "__main__":
    main()
