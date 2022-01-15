"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
"""
from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squared_nums = [num ** 2 for num in nums]
        squared_nums.sort()
        return squared_nums

answer = Solution()
test_number = [-4,-1,0,3,10]
print('Expected Output: [0, 1, 9, 16, 100]')
print(f'Actual Output: {answer.sortedSquares(test_number)}')