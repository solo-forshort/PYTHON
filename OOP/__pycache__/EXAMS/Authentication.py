class Auth:     
    def login(self):
        pass
        

class Pass(Auth):
    def __init__(self, pword = "admin123", uname = "admin" ):
        self.pword = pword
        self.uname = uname
        
    def login(self):
        print("Pass class Method!\n")
        username = input("Enter username: ")
        password = input("Enter Password: ")
        if username == self.uname and password == self.pword:
            print("Access granted. Authentication successful,")
        else:
            print("Incorrect username or password.")
            print("Authentication failed")
        print("-" * 40)


class Pin(Auth):
    def __init__(self, pword = "1234", uname = "admin"):
        self.pword = pword
        self.uname = uname

    def login(self):
        print("\nPin class Method!\n")
        username = input("Enter username: ")
        PIN = input("Enter a 4-digit Pin: ")
        if username == self.uname and PIN == self.pword:
            print("Access granted. Authentication successful")
        else:
            print("Access denied. Authentication failed")
        print("-" * 40)
 
authentication = [Auth(), Pass(), Pin()]
for authen in authentication:
    authen.login()