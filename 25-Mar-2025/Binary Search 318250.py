# Problem: Binary Search - https://leetcode.com/problems/binary-search/description/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        n = len(nums)

        low  = 0
        high = n - 1
        mid = (low + high) // 2

        while  low <= high:
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
                
            mid = (low + high) // 2

        return -1

