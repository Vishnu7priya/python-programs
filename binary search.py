def binary_search(key,arr):
    f=0
    l=len(arr)-1
    while f<=l:
        mid=(f+l)//2
        if arr[mid]==key:
            return f"{key} found in the index of {mid}"
        if arr[mid]<key:
            f=mid+1
        else:
            l=mid-1
    return "Not found"
arr=[2,5,7,9,14,22]
print(binary_search(14,arr))
