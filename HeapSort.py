def heapify(arr,n,i):
    Largest = i
    Left = 2*i + 1
    Right = 2*i + 2

    if Left < n and arr[i]<arr[Left]:
        Largest = Left
    if Right < n and arr[Largest] < arr[Right]:
        Largest = Right

    if Largest != i:
        arr[i],arr[Largest]=arr[Largest],arr[i]
        heapify(arr,n,Largest)

def heapSort(arr):
    n=len(arr)
    for i in range (n,-1,-1):
        heapify(arr,n,i)
    for i in range (n-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        heapify(arr,i,0)

arr=[12,43,1,3,88,90]
heapSort(arr)
for i in range (len(arr)):
    print(arr[i])