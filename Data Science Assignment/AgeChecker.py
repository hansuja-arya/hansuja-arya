n=int(input("Enter your Age : "))
if n<0:
    print("Enter a Valid age")
elif n>18:
    print("You are eligible to Vote\nApply for Driving License")
else:
    print("You are not eligible")