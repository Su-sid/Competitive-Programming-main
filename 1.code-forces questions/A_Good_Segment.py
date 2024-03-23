n = int(input())  
s = input()  
final = length = 1  
for i in range(1, n):
    if ord(s[i]) == ord(s[i - 1]) + 1:
        length += 1  
    else:
        final = max(final, length)  
        length = 1 
final = max(final, length)
print(final) 
