def Selection_sort(arr):
    for i in range(len(arr)-1):
        min=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min]:
                min=j
        if min!=i:
            arr[min],arr[i]=arr[i],arr[min]
    return arr
arr=[7,3,5,9,10,8]
print(Selection_sort(arr))
