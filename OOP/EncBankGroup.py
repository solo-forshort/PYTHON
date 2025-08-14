import os
class AccountSecured:
    def __init__(self, user_pin, balance):
        self.__your_pin = user_pin
        self.balance = balance
        self.attempts = 0
        self.__locked = False

    def balance_checker(self):
        USER_PIN = input("Enter user pin: ")
        if self.__locked == True:
            print("Account is locked. Access denied")
            return

        if USER_PIN  == self.__your_pin:
            print(f"Your balance is {self.balance}")
            self.attempts = 0
        else:
            self.attempts += 1
            print("Access denied, Incorrect Pin.")
            if self.attempts >= 3:
                self.__locked = True
                print("Account locked after 3 failed attempts.")
            


    def change_USER_PIN(self):
        old_pin = input("Enter your old pin: ")
        new_pin = input("Enter new pin: ")
        if self.__locked:
            print("Cannot change Pin, Account is locked.")
            return


        if old_pin == self.__your_pin:
            self.__your_pin = new_pin
            print("Pin changed succesfully.")
        else:
            print("Pin change unsucessful, Incorrect old Pin")

    def account_masking(self):
        masking = "****" + self.__your_pin[-4:]
        print(f"Masked account information: {masking} ")

#Running the code
#Onjects are created in a different file for easier **Testing

