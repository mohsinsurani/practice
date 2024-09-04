from typing import List
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count the frequencies of each element
        freq_map = Counter(nums)
        
        # Step 2: Use a heap to find the k most frequent elements
        # heapq.nlargest will give us the k elements with the highest frequencies
        most_frequent = heapq.nlargest(k, freq_map.keys(), key=freq_map.get)
        
        return most_frequent

# Example usage
solution = Solution()
print(solution.topKFrequent([1,1,1,2,2,3], 2))  # Output: [1, 2]
# print(solution.topKFrequent([1], 1))           # Output: [1]
