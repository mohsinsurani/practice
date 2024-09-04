# Maximum of all subarrays of size k | Sliding Window

from typing import List
from collections import deque

# get the maximum of all subarray of window size 3
def get_max_sub_array(arr: List[int], k: int):
    i = 0
    j = 0

    deq = deque()
    max_arr: List[int] = []

    while (j < len(arr)):
        while deq and arr[deq[-1]] < arr[j]:
            deq.pop()

        deq.append(j)

        if (j-i+1) < k:
            j += 1 # to dynamically keep the window
        elif (j-i+1) == k: # as window size fixes
            max_arr.append(arr[deq[0]])

            if deq[0] == i:
                deq.popleft()

            i += 1
            j += 1 

    print(max_arr)

arr = [1, 3, -1, -3, 5, 3 ,6, 7]
k = 3 # window size
get_max_sub_array(arr=arr, k=k)