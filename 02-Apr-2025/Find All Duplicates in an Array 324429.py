# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        l , r = 0 , 1
        nums.sort()

        ans  = []
        while r < n:

            if nums[l] == nums[r]:
                ans.append(nums[l])

            l += 1
            r += 1

        return ans



