def square(x):
    return x*x
num = [1,2,3,4,5,6,7,8,9]
print(tuple(map(square,num)))

'''Map function can receive 
a named function and a iterative,
like list\ tuple. It can use the iterative items 
by applying that function.'''