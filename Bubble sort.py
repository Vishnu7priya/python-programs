def bubblesort(arr):
    for phase in range(len(arr)-1):
        check=True
        for j in range(len(arr)-1-phase):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                check=False
        if check: return arr
    return arr
arr=[3,17,1,25,8,22]
print(bubblesort(arr))
