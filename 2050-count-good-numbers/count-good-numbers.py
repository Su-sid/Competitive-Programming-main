class Solution:
    def countGoodNumbers(self, n: int) -> int:

        MOD= 10**9 +7

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
        
        odd=n//2

        even=n//2+n%2

        return (pow(5, n//2+n%2, MOD)  * pow(4,(n//2), MOD)) % MOD
            #$ ((pow(5,even,mod)*pow(4,odd, mod))%mod)        
           































        # def is_prime(n):
        #     if n <= 1:
        #         return False
        #     for i in range(2, (n**n) + 1):
        #         if n % i == 0:
        #             return False
        #     return True