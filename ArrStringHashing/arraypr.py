from typing import List

def findPairForSum(nums: List[int], target: int) -> List[int]:
    num_map = {}
    
    # Populate the dictionary with the number as the key and its index as the value
    for index, element in enumerate(nums):
        num_map[element] = index
    
    # Loop through the list to find the pair
    for i in range(len(nums)):
        complement = target - nums[i]
        
        # Check if the complement exists and is not the same element
        if complement in num_map and num_map[complement] != i:
            return [i, num_map[complement]]
    
    return []

# Test the function
arre = [0, 2, 3, 4, 6]
target = 7
print(findPairForSum(arre, target))  # Expected output: [1, 4]
