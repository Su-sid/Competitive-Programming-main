
class Solution:
    def compress(self, chars: List[str]) -> int:

        count = 1
        j = 0
        if len(chars) == 1:
            return 1
        
        for i in range(1, len(chars) + 1):
            if i < len(chars) and chars[i] == chars[i - 1]:
                count += 1
            else:
                chars[j] = chars[i - 1]
                j += 1
                
                if count > 1:
                    for digit in str(count):
                        chars[j] = digit
                        j += 1
                count = 1
        
        return j
     