num1= int(input("Enter first number : "))
num2= int(input("Enter second number : "))
num3= int(input("Enter third number : "))

if num1>num2:
    if num1>num3:
        print(num1, "is bigger among this three.")
    else:
        print(num3,"is bigger among this three. ")
if num2>num1:
    if num2>num3:
        print(num2,"is bigger among this three.")
    else:
        print(num3,"is bigger among this three.")
