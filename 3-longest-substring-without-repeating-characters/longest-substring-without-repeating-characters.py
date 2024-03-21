class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        checker= dict()
        top=bottom=final=0
        length= len(s)
        while bottom < length:
            if s[bottom] in checker:
                top= max(checker[s[bottom]] +1  ,  top )
            checker[s[bottom]]= bottom
            final=max(final, bottom-top+1)
            bottom+=1
            # print(checker)
        
        return final
        