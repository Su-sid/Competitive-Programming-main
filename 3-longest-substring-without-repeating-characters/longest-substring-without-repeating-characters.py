class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s.strip()
        checker= dict()
        top=bottom=final=0
        length= len(s)

        # if s =="" and len(s)==0:
        #     final=0
        #     return final

        while bottom < length:

            if s[bottom] in checker:
                top= max(checker[s[bottom]] +1  ,  top )

            checker[s[bottom]]= bottom
            final=max(final, bottom-top+1)
            bottom+=1
        
        return final
        