def calculate_fine(days):
    fine = 0

    if days <= 0:
        fine = 0
    elif days <= 5:
        fine = days * 2
    elif days <= 10:
        fine = days * 5
    else:
        fine = days * 10

    return fine
days = int(input("Enter number of overdue days: "))
if days < 0:
    print("Days cannot be negative.")
else:
    total_fine = calculate_fine(days)
    print("Total Library Fine: ₹",total_fine)