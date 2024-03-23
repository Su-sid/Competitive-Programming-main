class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        uniq = set(word[0])
        result = 0
        current_length = 1
        l = 0
        for r in range(1, len(word)):
            if word[r] >= word[l]:
                uniq.add(word[r])
                current_length += 1
            else:
                uniq = set(word[r])
                current_length = 1
            if len(uniq) == 5:
                result = max(result, current_length)     
            l+= 1     
        return result

                    


            
        