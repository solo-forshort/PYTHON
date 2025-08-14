
def add(x, y):
    return x + y
def subtraction(x, y):
    return x - y
def multiplication(x, y):
    return x * y
def division(x, y):
    if y == 0:
        print("Error:cannot be divided by zero!")
    else:
        return x / y

print("Select option:")
print("1. Addition")
print("2. subtraction")
print("3. multiplication")
print("4. Division")

option = input("Enter option either: 1/2/3/4: \n")
num_1 = float(input("Enter first number: "))
num_2 = float(input("Enter second number: "))

if option == "1":
    print("Results:", add(num_1, num_2))
elif option == "2":
    print("Results:", subtraction(num_1, num_2))
elif option == "3":
    print("Results:", multiplication(num_1, num_2))
elif option == "4":
    print("Results:", division(num_1, num_2))
else:
    print("Invalid option: Enter numbers only..!")