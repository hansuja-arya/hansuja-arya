def bus_fare(age):
    fare_price=100
    if age<0:
        return -1
    elif age<5:
        return 0
    elif age<=17:
        return fare_price*0.5
    elif age>=60:
        return fare_price*0.7
    else:
        return fare_price
age=int(input("Enter your Age : "))
fare=bus_fare(age)
if fare==-1:
    print("Enter a Valid Age")
else:
    print("Ticket Price :",fare)