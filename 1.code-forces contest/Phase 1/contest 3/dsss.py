def divide_array(arr):
    # Initialize lists for negative, positive, and zero elements
    negative, positive, zero = [], [], []
    
    # Distribute the elements into the respective lists
    for num in arr:
        if num < 0:
            negative.append(num)
        elif num > 0:
            positive.append(num)
        else:
            zero.append(num)
    
    # Adjust the lists to meet the specific conditions
    # If the count of negative numbers is even, move one to positive to make the product of negatives < 0
    if len(negative) % 2 == 0:
        positive.append(negative.pop())
    
    # Ensure there is at least one positive if all were negative initially (and since a solution exists, there's at least one zero)
    if not positive:
        positive.append(negative.pop())
        positive.append(negative.pop())
    
    # Output the partitions
    print(len(negative), ' '.join(map(str, negative)))
    print(len(positive), ' '.join(map(str, positive)))
    print(len(zero), ' '.join(map(str, zero)))

# Example usage
n = int(input("Enter the number of elements: "))
arr = list(map(int, input("Enter the elements separated by space: ").strip().split()))
divide_array(arr)
