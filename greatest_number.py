

def find_greatest(num1, num2, num3):
    if num1>= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print("\nChecking The Greatest Number..\n")
a = float(input("Enter fisrt number:  "))
b = float(input("Enter second number:  "))
c = float(input("Enter third number:  "))

greatest = find_greatest(a, b, c)
print(greatest, ": is the greatest number")
