class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        list_t = list(t)
        for i in s:
            list_t.remove(i)
        return list_t[0]