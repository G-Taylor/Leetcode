""" 
Problem: Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.
For example, 121 is a palindrome while 123 is not.

""" 
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

answer = Solution() 
test_number = 23432
print(f'Is The Number {test_number} A Palindrome?: {answer.isPalindrome(test_number)}')