t = int(input())
for i in range(t):
    n = int(input())
    for j in range(n):
        for k in range(n):
            print(end="*")
        print()
    if (i < t-1):
        print()