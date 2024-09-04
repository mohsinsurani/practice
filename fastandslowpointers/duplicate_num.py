# Definition for singly-linked list.
from typing import List, Optional

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
        return -1


input_values = [11,3,4,21,21]

print(Solution().findDuplicate(input_values))