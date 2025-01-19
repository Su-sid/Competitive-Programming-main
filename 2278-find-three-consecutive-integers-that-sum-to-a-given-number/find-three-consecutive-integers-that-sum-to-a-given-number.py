class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        final= []
        
        if num%3==0:
            x=num //3
            final=  [x-1, x, x+1]
        return final

      