from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        max_area = 0

        while i < j:
            current_height = min(height[i], height[j])
            current_width = j - i
            current_area = current_height * current_width

            # Update max_area if the current area is larger
            max_area = max(max_area, current_area)  

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        
        print(max_area)

print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))