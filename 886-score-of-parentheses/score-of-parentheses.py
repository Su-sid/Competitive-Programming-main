class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        score = 0
        
        for char in s:
            if char == '(':
                stack.append(score)
                score = 0
            else:
                score = stack.pop() + max(2 * score, 1)
                
        return score

# class Solution:
#     def scoreOfParentheses(self, s: str) -> int:
#         stack= []

#         score= 0

#         for i in s:
#             if i =='(':
#                 stack.append(score)

#             else:

# class Solution:
#     def scoreOfParentheses(self, s: str) -> int:
#         stack = []
#         score = 0
        
#         for c in s:
#             if c=='(':
#                 stack.append(score)
#                 score = 0
#             else:
#                 score = 1 if score==0 else score*2
#                 score += stack.pop()
#             print(score)
#         return score
