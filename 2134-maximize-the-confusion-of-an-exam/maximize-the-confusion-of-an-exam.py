class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        max_c  = 0 
        l = 0 
        tc = 0 
        fc = 0 
        for r in range(len(answerKey)):
            if answerKey[r]=='T':
                tc+=1
            else:
                fc+=1
            
            while min(tc,fc)>k:
                if answerKey[l]=='F':
                    fc-=1
                else:
                    tc -=1
                l+=1
            max_c = max(r-l+1, max_c)
        return max_c