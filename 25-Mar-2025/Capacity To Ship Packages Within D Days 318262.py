# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def cheker(answer):
            curr_sum = 0
            days_count = 1
            for num in weights:
                curr_sum += num
                if curr_sum > answer:
                    days_count += 1
                    curr_sum = num
                    if days_count > days:
                        return False
            return True
        
        low, high = max(weights), sum(weights)


        while low <= high:
            mid = (low + high) // 2


            if  cheker(mid):
                high = mid - 1
            else:
                low = mid + 1

        return low