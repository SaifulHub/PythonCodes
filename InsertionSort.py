def insertionsort(arr):
    n=len(arr)
    for i in range(n):
        key=arr[i]
        j=i-1
        while j>=0 and key < arr[j]:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key

arr=[10,-8,23,41,9,77]
insertionsort(arr)
print("Sorted Array is:\n")
for i in range(len(arr)):
    print(arr[i])
