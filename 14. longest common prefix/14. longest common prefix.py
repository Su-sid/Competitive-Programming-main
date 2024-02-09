class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
     
        if not strs:  # Handle empty input list
            return ""

        shortest = min(strs, key=len)  # Find the shortest string
        for i, char in enumerate(shortest):
            for other in strs:
                if other[i] != char:
                    return shortest[:i]  
        return shortest 