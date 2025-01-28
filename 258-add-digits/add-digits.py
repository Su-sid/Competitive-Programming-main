class Solution:
    def addDigits(self, num: int) -> int:
      
        def rec(num):
            strNum = [int(i) for i in str(num)] 
            if len(strNum) <2:
                num = strNum[0]
                # print(num)
                return num
            return rec(sum(strNum))

        return rec(num)
            

            
            
        