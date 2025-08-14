User_Role = input("Please enter your posotion or role: \n")

if User_Role == "Admin":
    print("Access granted! Full system access.")
    print("You can add/remove users ")
    print("You can change system settings\n")

elif User_Role == "Staff":
    print("Access granted! Limited system Access.")
    print("You can add/remove users ")
    print("You can view/edit/delete all records \n")
    
elif User_Role == "Guest":
    print("Access granted! Read Only Access.")
    
else:
    print("Access denied! Contact Admin.")