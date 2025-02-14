class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        window=[]
        Acount=0
        num= str(num)
        for i in range(len(num)+1-k):
            window= num[i:i+k]
            div=int(window)
            if div !=0  and int(num) % div ==0: 
                Acount+=1
            
        return Acount

