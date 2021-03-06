def heapify(arr,n,i):
    large = i
    left = 2*i +1
    right = 2*i +2
    if left <n and arr[left]>arr[large]:
        large = left
    if right < n and arr[right]>arr[large]:
        large = right

    if large != i:
        arr[i],arr[large]=arr[large],arr[i]
        heapify(arr,n,large)

def deletion(arr,n):
    lastele = arr[n-1]
    arr[0]=lastele
    n=n-1
    heapify(arr,n,0)

arr= [10,5,3,2,4]
n=len(arr)
deletion(arr,n)
for i in range (n-1):
    print(arr[i])