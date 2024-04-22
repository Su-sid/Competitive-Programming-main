class Solution:
    def removeStars(self, s: str) -> str:
       
        stack = []
        for paran in s:
            if paran == '*' and stack:
                stack.pop()
            else : 
                stack.append(paran)

            # print(stack)
        return ''.join(stack)
