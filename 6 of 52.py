t = int(input())
for i in range(t):
    s = int(input())
    lsd = s %10
    msd = int(s/10000)
    print("Sum =",lsd+msd)