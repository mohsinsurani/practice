from typing import List

# get the maximum of all subarray of window size 3
def get_max_sub_array(arr: List[int], k: int):
    i = 0
    j = 0
    sum: int = 0
    maxVal: int = 0
    max_start_index = 0

    while (j < len(arr)):
        sum += arr[j]

        if (j-i+1) < k:
            j += 1 # to dynamically keep the window
        elif (j-i+1) == k: # as window size fixes
            if sum > maxVal:
                maxVal = sum
                max_start_index = i 

            sum -= arr[i]
            i += 1
            j += 1 

    print(maxVal)
    max_subarray = arr[max_start_index:max_start_index + k]
    print(max_subarray)


def get_max_sub_array_bf(arr: List[int], k: int):
    i = 0
    j = 0
    sum: int = 0
    maxVal: int = 0
    max_start_index = 0

    # Iterate over each possible starting index of the subarray of size `k`
    for i in range(len(arr) - k + 1):
        sum = 0
        # Calculate the sum of the subarray starting at index `i` and ending at `i + k - 1`
        for j in range(i, i + k):
            sum += arr[j]
        
        # Update maxVal and max_start_index if the current sum is greater than the maxVal found so far
        if sum > maxVal:
            maxVal = sum
            max_start_index = i


    print(maxVal)
    max_subarray = arr[max_start_index:max_start_index + k]
    print(max_subarray)


arr = [2, 5, 1, 8, 2, 9 ,1]
k = 3 # window size
get_max_sub_array_bf(arr=arr, k=k)