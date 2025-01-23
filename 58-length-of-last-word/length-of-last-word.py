class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        stringArr= list(map(str, s.split()))

        # print(stringArr)

        return (len(stringArr[-1]))
        