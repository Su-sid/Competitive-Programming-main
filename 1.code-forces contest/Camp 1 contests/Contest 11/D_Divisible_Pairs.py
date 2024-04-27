tests = int(input())
for _ in range(tests):
    n,x,y = list(map(int, input().split()))
    array = list(map(int, input().split()))
    count = {}
    beautiful_pairs = 0
    
    for num in array:
        mx = num % x
        my = num % y
        complement_x = (-mx) % x
        complement_y = my 
        
        if (complement_x, complement_y) in count:
            beautiful_pairs += count[(complement_x, complement_y)]
        
        if (mx, my) in count:
            count[(mx, my)] += 1
        else:
            count[(mx, my)] = 1

    print(beautiful_pairs)
