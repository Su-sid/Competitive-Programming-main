def maximum_removals_single_case(n, array):
    # Dictionary to count occurrences of each element
    count = {}
    for num in array:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    
    # sorted keys determine which elements to pick based on  current score
    sorted_keys = sorted(count.keys())
    
    
    result = []
    
    for initial in array:
        current_score = initial
        more_removes = 0
        # Copy of the count dictionary to modify during simulation
        temp_count = count.copy()
        temp_count[initial] -= 1  # Temporarily remove this element from the count
        
        for key in sorted_keys:
            while key <= current_score and temp_count[key] > 0:
                # How many times we can remove this element based on the current score
                num_removes = temp_count[key]
                more_removes += num_removes
                current_score += key * num_removes
                temp_count[key] = 0
        
        # Store the result for this initial element
        result.append(more_removes)
    
    print(' '.join(map(str, result)))


t = int(input())
for _ in range(t):
    n = int(input())
    test_case = list(map(int, input().split()))
    
    maximum_removals_single_case(n, test_case)
