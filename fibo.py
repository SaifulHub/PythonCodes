def find_fibbo(x):
    if x<=2:
        return 1
    fib1 = 1
    fib2 = 1
    i = 3
    while i <= x:
        i +=1
        fib1 ,fib2 = fib2,fib1+fib2
    return fib2

def list_fib(x):
    fib_list = [1,1]
    if x <=2:
        return fib_list[:x]
    fib1,fib2 = 1,1
    i =3
    while i<=x:
        i +=1
        fib1,fib2= fib2,fib1+fib2
        fib_list.append(fib2)
    return fib_list

for i in range(1,11):
    print (find_fibbo(i))
print(list_fib(1))
print(list_fib(2))
print(list_fib(10))
