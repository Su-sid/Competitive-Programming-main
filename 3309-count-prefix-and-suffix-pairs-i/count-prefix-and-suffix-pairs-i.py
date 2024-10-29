class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(str1, str2): 
            len_str1 = len(str1)
            # print(len_str1)
            pref = str2[:len_str1]
            suff = str2[-len_str1:]
            
            if not (pref== suff==str1):
                return False
            return True    
        i= 0 
        # j = 1
        tally=0
        words_len= len(words)   

        for i in range(words_len):
            str1= words[i]
            j = i+1
            # print(str1)
            while j < words_len:
                str2= words[j]
                # print((str1, str2))
                if isPrefixAndSuffix(str1, str2):
                    tally+=1
                j +=1
            # tally+=1
            # i +=1

        return tally

        


