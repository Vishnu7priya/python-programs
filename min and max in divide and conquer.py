def find_min(arr, s, e):
    if s == e:
        return arr[s]
    mid = (s + e) // 2
    left = find_min(arr, s, mid)
    right = find_min(arr, mid + 1, e)
    return min(left,right)
def find_max(arr, s, e):
    if s == e:
        return arr[s]
    mid = (s + e) // 2
    left = find_max(arr, s, mid)
    right = find_max(arr, mid + 1, e)
    return max(left,right)

arr = [3,1,2,7,5,9,8]
min = find_min(arr, 0, len(arr) - 1)
max=find_max(arr, 0, len(arr) - 1)
print(min)
print(max)
