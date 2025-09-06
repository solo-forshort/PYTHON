def bmiComputer():
    w = float(input("Enter your weight in Kilograms: "))
    h = float(input("Enter your height in meters: "))
    BMI = w / h**2

    if BMI < 18.5:
        print(f"Your BMI is {BMI:.2f}. You are underweight.")
    elif 18.5 <= BMI < 24.9:
        print(f"Your BMI is {BMI:.2f}. You have a normal weight.")
    elif 25 <= BMI < 29.9:
        print(f"Your BMI is {BMI:.2f}. You are overweight.")
    else:
        print(f"Your BMI is {BMI:.2f}. You are obese.")

bmiComputer()