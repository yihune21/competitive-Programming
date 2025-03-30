# Problem: 132 Pattern - https://leetcode.com/problems/132-pattern/

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        if len(nums) < 3:
            return False
        
        stack = []
        nums_k = float('-inf')
        for num in reversed(nums):
            
            if num < nums_k:
                return True
                
            while stack  and stack[-1] < num:
                nums_k = stack.pop()

            stack.append(num)
        return False




