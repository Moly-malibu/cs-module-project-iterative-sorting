#linear search.

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1   # not found

# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    low = 0
    hight = len(arr)-1
    mid = 0
    while hight >= low:
        mid = (hight + low) // 2
        if arr[mid] > target:
            hight = mid -1
        elif arr[mid] < target:
            low = mid + 1
        else:
            return mid
    return -1  # not found
