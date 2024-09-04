from typing import List

def subarraySum(nums: List[int], k: int) -> int:
    count = 0
    cumulative_sum = 0
    sum_freq = {0: 1}  # To handle subarrays that sum to k from the start

    for num in nums:
        cumulative_sum += num
        
        # Check if there is a previous cumulative sum that makes the current sum equal to k
        if cumulative_sum - k in sum_freq:
            count += sum_freq[cumulative_sum - k]
        
        # Update the frequency of the current cumulative sum in the hashmap
        if cumulative_sum in sum_freq:
            sum_freq[cumulative_sum] += 1
        else:
            sum_freq[cumulative_sum] = 1

    return count


arr = [1, 2, 1, 2, 1]
k = 3
subarraySum(arr, k)  # Output: 4
