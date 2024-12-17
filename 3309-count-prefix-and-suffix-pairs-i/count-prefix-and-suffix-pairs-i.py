class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(str1, str2): 
            len_str1 = len(str1)
            len_str2 = len(str2)
         
            pref = str2[:len_str1]
            suff = str2[-len_str1:]

            if len_str1 > len_str2:
                return False
            
            if not (pref== suff==str1):
                return False
            return True    

        count=0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if isPrefixAndSuffix(words[i], words[j]):
                    count+=1
        return count

        


