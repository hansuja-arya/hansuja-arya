x=float(input("Enter a Number : "))
y=float(input("Enter a Number : "))
z=input("Enter a operator('+,-,/,*') : ")
if z=='+':
    print(x,z,y,"=",x+y)
elif z=='-':
    print(x,z,y,"=",x-y)
elif z=='*':
    print(x,z,y,"=",x*y)
elif z=='/':
    print(x,z,y,"=",x/y)
else:
    print("Invalid Operator")