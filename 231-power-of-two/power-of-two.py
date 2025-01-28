class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        # return True if n %2==0 or n == 1 else False 
        return True if n>0 and bin(n).count('1') == 1 else False