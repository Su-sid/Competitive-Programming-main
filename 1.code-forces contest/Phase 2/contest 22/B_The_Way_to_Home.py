# Reading input
n, d = map(int, input().split())
s = input().strip()
jumps = 0
index = 0
    
while index < n - 1:
   
    farthest = index
    for i in range(index + 1, min(index + d + 1, n)):
        if s[i] == '1':
            farthest = i
    
   
    if farthest == index:
        print( -1)
    
   
    index = farthest
    jumps += 1
    
    
    if index == n - 1:
        print( jumps)
    
# print( jumps)