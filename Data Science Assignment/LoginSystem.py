c_username = "admin"
c_password = "admin"
attempts = 3

while attempts > 0:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == c_username and password == c_password:
        print("Login successful!")
        break
    else:
        attempts -= 1
        print("Incorrect. Attempts left:",attempts)

        if attempts == 0:
            print("Account locked. Please try again later.")