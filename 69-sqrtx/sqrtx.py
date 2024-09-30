class Solution:
    def mySqrt(self, x: int) -> int:
        
        

        def rec(x):
            left, right= 0, x
            
            while left <=right:
                mid=(left+ (right-left)//2)
                # print("left",left,"right",right,"mid", mid)
                if mid * mid == x:
                    return mid
                if mid * mid < x:
                    left= mid+1
                # elif mid * mid > x :
                else:
                    right= mid-1

                # return mid
            return right


        return rec(x)
        # return 0
        