# Problem: Predict the Winner - https://leetcode.com/problems/predict-the-winner/

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        def winner(arr , start , end):
            if start > end:
                return 0

            choice_1 = arr[start] - winner(arr , start + 1 , end)
            choice_2 = arr[end] - winner(arr , start , end - 1)

            return max(choice_1 , choice_2)
            
        res = winner(nums , 0 , len(nums) -1)

        return res >= 0
            



