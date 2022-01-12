"""
Given an array of integers nums which is sorted in ascending order, and an integer target, 
write a function to search target in nums. 

If target exists, then return its index. Otherwise, return -1.
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            return -1

    
answer = Solution()
print(f'Target found at index {answer.search([-2, 3, 5, 6, 9, 11], 9)}')