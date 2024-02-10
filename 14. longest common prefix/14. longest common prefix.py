class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix="" 
        shortest_string= min(strs, key=len)
  
        for i in range(len(shortest_string)): 
            for other_strings in strs:
                if not other_strings[i]== shortest_string[i]:
                    return prefix
                
            prefix+=shortest_string[i]
        return prefix
       
