def quick_sort(arr,left,right):
    if left<right:
        p_i = partition(arr,left,right)
        quick_sort(arr,left, p_i-1)
        quick_sort(arr,p_i + 1 , right)
 
def partition(arr,left,right):
 
    i=left
    pivot=arr[right]
    j=right-1
 
    while i<j:
        while i<right and arr[i]<pivot:
            i += 1
        while j>left and arr[j]>=pivot:
            j -= 1
        if i < j:
            arr[i],arr[j]=arr[j],arr[i]
    if arr[i]>pivot:
        arr[i],arr[right]=arr[right],arr[i]
    return i

arr=[7,4,15,22,8,1]
print(quick_sort(arr,7,8))
