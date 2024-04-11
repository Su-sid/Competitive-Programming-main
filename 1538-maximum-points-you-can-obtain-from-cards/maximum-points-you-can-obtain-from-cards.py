class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        length = len(cardPoints) - k
        prefix = sum(cardPoints[:length])
        tmp = sum(cardPoints) - prefix
        max_sum = tmp
        left = 0
        
        while length < len(cardPoints):
            tmp = tmp + cardPoints[left] - cardPoints[length]
            max_sum = max(max_sum,tmp)
            length +=1
            left +=1
            
        return max_sum