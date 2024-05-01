class Solution:
    def isPowerOfFour(self, n: int) -> bool:
       if  n==0: 
        return False
       if n==1 :#or n%4 ==0: 
        return True
    #    if n%4==0:
    #     return True
       return self.isPowerOfFour(n/4) #if n%4==0 else False
