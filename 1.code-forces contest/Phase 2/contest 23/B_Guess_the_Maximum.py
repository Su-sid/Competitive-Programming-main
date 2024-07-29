def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        arr = list(map(int, data[index:index+n]))
        index += n
        
        # To find the smallest maximum among all subarrays starting from each position to the end
        min_of_max = float('inf')
        
        # We iterate from the second to last element back to the first element
        for start in range(n - 2, -1, -1):
            # Initialize current maximum for subarrays starting at 'start'
            current_max = arr[start]
            
            # We iterate from the start to the end of the array
            for end in range(start + 1, n):
                current_max = max(current_max, arr[end])
            
            # Update the minimum of the maximum values found
            min_of_max = min(min_of_max, current_max)
        
        # The largest k for which Alice is guaranteed to win
        k = min_of_max - 1
        print(k)

# This function can be called as needed, making sure input redirection is properly set up
solve()
