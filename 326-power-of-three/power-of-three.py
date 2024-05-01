class Solution:
    def isPowerOfThree(self, n: int) -> bool:

        #base case
        if n==1:
            return True

        #recursive relation
        if n<=0 or n%3!=0 :
            return False

        #function call 
        return self.isPowerOfThree(n/3)