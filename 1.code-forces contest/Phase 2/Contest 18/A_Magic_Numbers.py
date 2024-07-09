

def finder(s):

    i = 0
    while i < len(s):
        if s[i] == '1':
            if i + 2 < len(s) and s[i + 1] == '4' and s[i + 2] == '4':  
                i += 3
            elif i + 1 < len(s) and s[i + 1] == '4': 
                i += 2
            else:  
                i += 1
        else:
            return "NO"
    return "YES"


n = input()
print(finder(n))
