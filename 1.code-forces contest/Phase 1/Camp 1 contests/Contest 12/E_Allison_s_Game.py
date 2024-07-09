n = int(input())
heights = list(map(int, input().split()))
   
heights.append(0)
stack = []
max_side = 0

for i, height in enumerate(heights):
    
    while stack and heights[stack[-1]] > height:
        H = heights[stack.pop()]
        W = i if not stack else i - stack[-1] - 1
    
        max_side = max(max_side, min(H, W))
    stack.append(i)
    
    # print(stack)

print(max_side) 
