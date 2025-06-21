def calculate_bill(units):
    bill = 0
    if units <= 100:
        bill = units * 1.5
    elif units <= 200:
        bill = units * 2.5
    elif units <= 300:
        bill = units * 4
    else:
        bill = units * 6

    return bill
units = int(input("Enter electricity units consumed: "))
if units < 0:
    print("Units cannot be negative.")
else:
    total = calculate_bill(units)
    print("Electricity Bill for",units,"units: ₹",total)