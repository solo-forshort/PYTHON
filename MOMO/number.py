password = "han22"
attempts = 0
## using while-loop
while attempts < 3:
    your_pass = input("Enter your password: ")
    if your_pass == password:
        print("Acess granted.")
        break
    else:
        print("Access denied.")
        attempts += 1
else:
    print("Account locked.")
