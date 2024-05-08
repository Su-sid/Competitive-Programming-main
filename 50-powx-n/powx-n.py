class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        #condition
        if x!=0 or n>0:
            return x**n

        #recursive state
        return self.myPow(x,n-1)


        