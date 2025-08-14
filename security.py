
import math

## Error Handling

try:
    num_1 = int(input("Enter number 1: "))
    num_2 = int(input("Enter number 2: "))
    print("Number_1 divided by number_2 is : ",num_1/num_2)
except ValueError:
    print("Plaese enter valid numbers")
except ZeroDivisionError:
    print("Cannot divide by zero")