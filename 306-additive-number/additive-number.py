class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def is_valid_sequence(num1, num2, remaining):
            while remaining:
                sum_str = str(int(num1) + int(num2))
                if not remaining.startswith(sum_str):
                    return False
                remaining = remaining[len(sum_str):]
                num1, num2 = num2, sum_str
            return True
        
        n = len(num)
        for i in range(1, n):
            for j in range(i + 1, n):
                num1, num2 = num[:i], num[i:j]
                if (len(num1) > 1 and num1[0] == '0') or (len(num2) > 1 and num2[0] == '0'):
                    continue
                if is_valid_sequence(num1, num2, num[j:]):
                    return True
        return False