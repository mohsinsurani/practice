from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        cons_sum = 0
        while (j < len(numbers)):
            cons_sum = numbers[i] + numbers[j]

            if cons_sum == target:
                return [i+1, j+1]
            elif cons_sum < target:
                i += 1  # Move the left pointer to the right to increase the sum
            else:
                j -= 1 
                
        return []


solution = Solution()
print(solution.twoSum([2,3,4], 6))  # need one plus index array as o/p