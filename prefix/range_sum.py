def prefix_sum(arr):
    n = len(arr)
    prefix = [0] * n
    prefix[0] = arr[0]

    for i in range(1, n):
        prefix[i] = prefix[i - 1] + arr[i]

    return prefix

# Example usage:
arr = [2, 4, 6, 8, 10]
prefix = prefix_sum(arr)
print(prefix)  # Output: [2, 6, 12, 20, 30]

# Sum of subarray from index 1 to 3 (4 + 6 + 8):
subarray_sum = prefix[3] - prefix[0]  # Output: 18
print(subarray_sum)
