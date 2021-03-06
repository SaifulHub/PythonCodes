def First(n):
    while n>=10:
        n=n/10
    return int(n)
def Last(n):
    return int(n%2)
n=54123
print(First(n))
print(Last(n))