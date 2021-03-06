num = int(input("Enter a number to find grade : "))
if num>80:
    print("Grade is A+")
elif num>70:
    print("Grade is A")
elif num>60:
    print("Grade is A-")
elif num>50:
    print("Grade is B")
elif num>40:
    print("Grade is C")
elif num>=30:
    print("Grade is D")
else:
    print("Fail.")