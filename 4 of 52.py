def kisu(T):
    for i in range (T):
        N=int(input())
        print("Case",i+1,end=": ")
        for j in range(1,N,1):
            if(N%j==0):
                print(j,end=" ")
        print(N)
T = int(input())
kisu(T)