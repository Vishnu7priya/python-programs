def linear_search(key,arr):
    for i in range(len(arr)):
        if key==arr[i]:
            return "search successful"
    return "key not found"

arr=[2,5,7,14,9,22]
print(linear_search(14,arr))
    
