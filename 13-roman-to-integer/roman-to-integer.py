class Solution:
    def romanToInt(self, s: str) -> int:
        romanMap= {
            'I':1,
            # 'IV':4,
            'V':5,
            # 'IX':9,
            'X':10,
            # 'XL':40,
            'L':50,
            # 'XC':90,
            'C':100,
            # 'CD':400,
            'D':500,
            # 'CM':900,
            'M':1000
        }
        total= 0 
        k = len(s)

        for i in range(k):
            if i+1 < k and romanMap[s[i]] < romanMap[s[i+1]]:
                total-= romanMap[s[i]]
            else:
                total+= romanMap[s[i]]

        return total

