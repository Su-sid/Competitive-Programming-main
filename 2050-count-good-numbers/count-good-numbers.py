class Solution:
    def countGoodNumbers(self, n: int) -> int:
        # even =[0,2,4,6,8]

        # odd=[2, 3, 5, 7]
        MOD= 10**9 +7

        count=1 

        if n % 2 ==0:
            count*= pow(4,(n//2),MOD)

            count*= pow(5,(n//2),MOD)

            
            count%= MOD
            
        else:
            count*= pow(4,(n//2),MOD)

            count*= pow(5,(n+1)//2,MOD)

            count%=MOD
            print(count)
            
        return count
            
           































        # def is_prime(n):
        #     if n <= 1:
        #         return False
        #     for i in range(2, (n**n) + 1):
        #         if n % i == 0:
        #             return False
        #     return True