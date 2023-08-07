class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid_string=[]
        for i in s:
            if i.isalnum():
                valid_string.append(i.lower())
            else:
                continue
        right=len(valid_string)-1
        left=0
        while left<right:
            if valid_string[left]!=valid_string[right]:
                return False
            right-=1
            left+=1
            
        return True