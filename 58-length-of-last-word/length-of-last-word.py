class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        last_word = s.split()

        return len(last_word[-1])
        