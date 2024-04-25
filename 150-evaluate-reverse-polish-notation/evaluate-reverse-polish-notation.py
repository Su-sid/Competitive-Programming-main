class Solution:
# Push all numbers to stack.
# When encountering an operator pop last 2 from stack and perform operation.
# Push result of that operation back to stack and continue.
# Return number at top of stack when done.
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        final=0

        for token in tokens:
            if token == '+':
                op1, op2= stack.pop(),stack.pop()
                stack.append(op1 + op2)

            elif token=='-':
                op1, op2= stack.pop(),stack.pop()
                stack.append(op2 - op1)

            elif token=='*':
                op1, op2= stack.pop(),stack.pop()
                stack.append(op1 * op2)

            elif token== '/':
                op1, op2= stack.pop(),stack.pop()
                stack.append(int(op2 / op1))

            else:
                stack.append(int(token))
            # print(stack)    
        return stack[0]
               