t = int(input())
results = []

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    # The key here is to recognize that Alice's optimal strategy is to choose the second highest element in the array.
    # Bob's strategy will be to choose the maximum segment. So Alice wins if k is less than the maximum of any segment.
    # Thus, the largest k where Alice wins is the second highest element in the array.
    
    max1 = max(a)  # The maximum element in the array
    max2 = -1  # Initialize the second maximum element
    
    for num in a:
        if num != max1:
            if max2 == -1 or num > max2:
                max2 = num

    results.append(max2)

for result in results:
    print(result)