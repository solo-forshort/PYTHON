class SimpleInterest:
    def __init__(self, prin, rate, time):
        self.prin = prin
        self._rate = rate
        self.__time = time 


    def gettime(self):
        print(f"The time is {self.__time} \n")
    
    def settime(self):
        try:
            current_time = float(input("Enter the time period: "))
            self.__time = current_time
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    def calc_SI(self):
        SI = (self.prin * self._rate * self.__time) / 100
        print(f"The simple interest is: {SI} \n")
        

principal = float(input("\nEnter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time period in years: "))
print("-" * 40)



calcul = SimpleInterest(principal, rate, time)
def main():
    print("MENU")
    print("1. Calculate Simple Interest")
    print("2. Get Time Period")
    print("3. Set Time Period")
    print("4. Exit")
    while True:
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            calcul.calc_SI()
        elif choice == '2':
            calcul.gettime()
        elif choice == '3':
            calcul.settime()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Enter or choose from 1 to 4 only.")
if __name__ == "__main__":
    main()
# calcul.calc_SI()
# calcul.gettime()
# calcul.settime()
# calcul.calc_SI()