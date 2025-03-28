# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        points.sort(key = lambda p : p[1])
        start , i = points[0][1] , 0
        res = 1
        while i < len(points):

            if points[i][0] > start:
                res += 1
                start = points[i][1]
            
            i += 1
            
        return res

        