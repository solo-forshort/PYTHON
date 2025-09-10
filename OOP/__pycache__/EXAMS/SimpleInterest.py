class SimpleInterest:
    def __init__(self, prin, rate, time):
        self.prin = prin
        self._rate = rate
        self.__time = time 


    def gettime(self):
        print("The time is {self.__time}")
    
    def settime(self):
        current_time = input("Enter the time period: ")
        self.__time  = current_time

    def calc_SI(self):
        SI = (self.prin * self._rate * self.__time) / 100
        print(f"The simple interest is: {SI} ")

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time period in years: "))



calcul = SimpleInterest(principal, rate, time)
calcul.calc_SI()