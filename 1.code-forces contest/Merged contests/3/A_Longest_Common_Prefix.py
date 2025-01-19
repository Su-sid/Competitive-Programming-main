n = int(input())
if n < 2:  
    print(0)

first = input()
if len(first) < 1: 
    print(0)

prefix_length = len(first)  

for _ in range(n-1):
    current = input()
    
    current_match = 0
    for i in range(min(prefix_length, len(current))):
        if first[i] != current[i]:
            break
        current_match += 1
    
    prefix_length = min(prefix_length, current_match)

print(prefix_length)