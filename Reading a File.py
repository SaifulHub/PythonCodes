info = open("Information.txt","r")
user = input("Do you wanna see the information? ")
if (user =="yes" or user =="Yes" or user =="YES"):
    print(info.read())
elif(user =="yEs" or user == "YEs" or user =="yeS"or user =="yES"or user =="YeS"):
    user = input("Correct your spelling and Case.")
    if(user =="yes" or user =="Yes" or user =="YES"):
        print(info.read())
else:
    print("Thanks.")