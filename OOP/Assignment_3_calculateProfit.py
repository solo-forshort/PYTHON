import math

def calculateProfit():
    selling_price = float(input("Enter selling price of item: "))
    cost_price = float(input("Enter cost price of item: "))

    profit = selling_price - cost_price
    print(f"Your profit is {profit} cedis")

calculateProfit()