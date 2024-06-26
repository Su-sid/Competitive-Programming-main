class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        
        shifts = list(accumulate(shifts[::-1]))

        res = []
        for c, k in zip(s, shifts[::-1]):
            pos = (ord(c) - 97 + k) % 26 + 97
            res.append(chr(pos))

        return ''.join(res)