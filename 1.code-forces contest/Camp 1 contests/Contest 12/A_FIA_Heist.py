line = input()

stack = []
i = 0
while i < len(line):
    if line[i] == "<":
        if i + 1 < len(line) and line[i + 1] == "-":
            if stack:
                stack.pop()
            i += 1 
    else:
        stack.append(line[i])
    i += 1

final = ''.join(stack)
print(final)
