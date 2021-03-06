def bubblesort(ar):
    n=len(ar)
    for i in range(n):
        for j in range(0,n-i-1):
            if ar[j]>ar[j+1]:
                ar[j],ar[j+1]=ar[j+1],ar[j]
arr=[10,9,5,4,2,22,18]
bubblesort(arr)
print("Sorted array is :\n")
for i in range (len(arr)):
    print(arr[i])