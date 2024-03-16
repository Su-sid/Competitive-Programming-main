class Solution:

    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        result_string = "".join(word1)
        result_string2 = "".join(word2)
        
        if not result_string == result_string2:
            return False
        return True


        