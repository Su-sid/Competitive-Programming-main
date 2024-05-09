# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left ,right=1, n
        
        # two pointer to check the list.
        while left< right:
            mid= left + (right - left) // 2
            
            #condition to check bad batch 
            if isBadVersion(mid):
                right= mid
            else :
                left= mid+1
        return left


