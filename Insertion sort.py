def insertion_sort(arr):
    for i in range(1,len(arr)):
        j=i-1
        temp=arr[i]
        while j>=0 and arr[j]>temp:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=temp
    return arr

arr=[12,7,18,22,4,6,15,2]
print(insertionsort(arr))
