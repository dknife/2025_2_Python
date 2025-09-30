def quicksort(arr):
    """Sort a list using the recursive quicksort algorithm."""
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    
    left = []
    right = []

    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    return quicksort(left) + [pivot] + quicksort(right)

# Example usage

numbers = [86, 58, 12, 78, 51, 45, 80, 22, 23, 94, 24, 42, 58, 60, 96, 37, 6, 3, 87, 4, 41, 44, 15, 68, 14, 76, 55, 4, 89, 95, 80, 74, 18, 33, 18, 83, 42, 23, 96, 90, 52, 22, 6, 80, 78, 29, 56, 82, 57, 73, 73, 25, 54, 94, 9, 89, 3, 48, 54, 97, 55, 61, 28, 7, 49, 86, 61, 96, 45, 87, 7, 73, 74, 60, 82, 80, 100, 93, 61, 83, 87, 97, 74, 86, 75, 73, 49, 6, 11, 39, 64, 16, 37, 99, 84, 62, 27, 10, 7, 21]
sorted_numbers = quicksort(numbers)
print(sorted_numbers)  # Output: [1, 2, 5, 5, 6, 9]

numbers.sort()
print(numbers)  # Output: [1, 2, 5, 5, 6, 9]