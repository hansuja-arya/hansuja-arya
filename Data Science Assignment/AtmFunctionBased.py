def atm():
    print("\t\t\t\tWelcome to HDFC ATM")
    amount = 90000
    pin = "8700"
    card1 = input("Insert your card: ")
    card=card1.lower()
    if card:
        print("Welcome!")
        entered_pin = input("Enter your pin: ")
        if entered_pin == pin:
            print("\n\t\t\t1) Check Balance\n\t\t\t2) Cash Withdraw")
            option = int(input("Select your option: "))
            if option == 1:
                print("Your current balance is:", amount)
            elif option == 2:
                user_amount = int(input("Enter your amount: "))
                if user_amount <= amount:
                    print("Your balance is:", amount - user_amount)       
                else:
                    print("Insufficient funds.")  
            else:
                print("Invalid option selected.")
        else:
            print("Wrong pin")
    else:
        print("Invalid card")
atm()