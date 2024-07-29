
def validPar( s):
    stack = []
    store = {
        ')': '('
    }
    count= 0
    for paran in s:
        if paran in ('('):
            stack.append(paran)

        elif stack and store[paran] == stack[-1]: 
            stack.pop()
            count+=2
        else:
            continue 
    return print(count)


s=  input()
# print(s)
validPar(s)