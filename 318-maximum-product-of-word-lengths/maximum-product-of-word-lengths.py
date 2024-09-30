class Solution:
    def maxProduct(self, words: List[str]) -> int:

        n = len(words)

        bitmask = [0 for x in range(n)]

        for x in range(n):
            word = words[x]
            for letter in word:
                bitmask[x] = bitmask[x] | 1 << (ord('z') - ord(letter))
        
        score = 0
        
        for i in range(n):
            for j in range(i+1, n):
                if not (bitmask[i] & bitmask[j]):
                    score = max([score, len(words[i])*len(words[j])])

        return score
                