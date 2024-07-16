t = int(input())

results = []

for _ in range(t):
    n = int(input())
    array = list(map(int, input().strip().split()))
    

    if n == 1:
        
        results.append(array[0] - 1)
        continue
    
    max1 = -1
    max2 = -1
    
    
    for value in array:
        if value > max1:
            max2 = max1
            max1 = value
        elif max1 > value > max2:
            max2 = value
    
    if max2 == -1: 
        results.append(max1 - 1)
    else:
        results.append(max2)

for result in results:
    print(result)
