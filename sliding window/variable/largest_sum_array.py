#Variable Size Sliding Window | Largest Subarray of sum K | Part1

from typing import List

# get the maximum window size from the subarray with target sum k
def get_largest_ws_sum_array(arr: List[int], k: int):
    i = 0
    j = 0
    sum = 0
    max_window_size = 0

    while (j < len(arr)):
        sum += arr[j]

        if sum < k:
            pass
        elif sum == k:
            max_window_size = max(max_window_size, j-i+1)
        else:
            while (sum > k):
                sum -= arr[i]
                if sum == k:
                    max_window_size = max(max_window_size, j-i+1)
                i += 1
        j += 1

    print(max_window_size)


arr = [1,2,1,2,1]
k = 3 # target sum
get_largest_ws_sum_array(arr=arr, k=k)