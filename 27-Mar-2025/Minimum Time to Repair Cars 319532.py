# Problem: Minimum Time to Repair Cars - https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:

        """
        i th man  r - rank takes r * n * n mins

        """

        
        def checker(time):
            t = 0
            for rank in ranks:
                t += int(sqrt(time/rank))
            if t >= cars:
                return True
            else:
                return False
         
        low , high = 0 , min(ranks) * cars * cars
        ans = high

        while low <= high:
            mid = (low + high) // 2  
            if checker(mid):
                high = mid - 1
                ans = min(ans,mid)
            else:
                low = mid + 1
        return ans