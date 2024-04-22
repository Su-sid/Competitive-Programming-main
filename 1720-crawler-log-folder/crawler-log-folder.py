class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for log in logs:
            if log not in ('../', './'):
                # print(log[:-1])
                stack.append(log[:-1])
            elif log == '../' and stack:
                stack.pop()
            else:
                continue
        return len(stack)
