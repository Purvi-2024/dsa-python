# Linear Search in Python

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

numbers = [5, 8, 2, 9, 1]
target = 9

result = linear_search(numbers, target)

if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")
