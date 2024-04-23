class Solution:
    def isValid(self, s: str) -> bool:
        if s[0] in (')', '}', ']'):
            return False
        stack = []
        par = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for paran in s:
            if paran in ('(', '[', '{'):
                stack.append(paran)

            elif stack and par[paran] == stack[-1]: 
                stack.pop()
            else:
                return False 
        return len(stack) == 0
