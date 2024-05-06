class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD= 10**9 +7

        return (pow(5, n//2+n%2, MOD)  * pow(4,(n//2), MOD)) % MOD
       
        # MOD= 10**9 +7
        # count=1 

        # if n % 2 ==0:
        #     count*= pow(4,(n//2),MOD)

        #     count*= pow(5,(n//2),MOD)

            
        #     count%= MOD
            
        # else:
        #     count*= pow(4,(n//2),MOD)

        #     count*= pow(5,(n+1)//2,MOD)

        #     count%=MOD
        #     print(count)

        # return count