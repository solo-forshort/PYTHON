

class AccountSecured:   ## class declared
    def __init__(self, pin): #constructor with 2 parameter
        self.__your_pin = pin  ##private attribute
        self.balance = 1000
        self.attempts = 0
        self.__locked = False  

    def Check_USER_PIN(self, user_pin): #method for checking user pin before dispaying balance
        if self.__locked: #check if account is locked first
            print("Account is locked due to multiple failed attempts.")
            return
        if user_pin == self.__your_pin: #when pin entered is correct
            print(f"Your balance is: {self.balance}cedis")
            self.attempts = 0     #reset attempts
        else:
            self.attempts += 1 #count number of attempts
            print("Access Denied: Incorrect Pin")
            if self.attempts >= 3: #locking account after 3 or more wrong attempts
                self.__locked = True
                print("Account locked after 3 failed attempts.")

    def change_pin(self, old_pin, new_pin):
        if self.__locked:     #check if account is locked first
            print("Cannot change Pin. Account locked.")
            return 
        if old_pin == self.__your_pin: #compare pin entered to old pin
            self.__your_pin = new_pin
            print("PIN successfully changed .")
            self.attempts = 0
        else:
            self.attempts += 1
            print("Incorrect old PIN.")
            if self.attempts >= 3:
                self.__locked = True
                print("Account locked after 3 failed attempts.")

    def account_masking(self): 
        masking = "****" + self.__your_pin[-4:] #takes the last characters of the pin
        print(f"Account PIN info: {masking}")
    ###### my_list = "12556"
    ###### my_list[-4]

## Example usage
#acount1 = AccountSecured("123456") #create an object/instance
# acount1.Check_USER_PIN("123456")    #methods on objects
#acount1.change_pin("1234", "0123456")
# acount1.account_masking()
