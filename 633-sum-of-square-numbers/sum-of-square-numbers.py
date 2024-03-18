class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        '''
        two pointer where start is 0 and the end is sqrt of c (as we have to iterate till sqrt of c).
        If sum (a^2+b^2) is equal to the sum then return true;
        Else if sum is greater than c then decrease the end;
        Else if sum is smaller than c then increase the start;
        '''

        # start = 0
        # end = int(c**2)

        # while start <= end:
        #     total = start**2 + end**2
        #     if total == c:
        #         return True
        #     if total > c:
        #         end -= 1
        #     else:
        #         start += 1

        # return False
 
        l, r = 0, int(c ** 0.5)
        while l <= r:
            lhs = l*l + r*r
            if lhs == c: return True
            if lhs < c: l += 1
            else: r -= 1
        return False