def minimum_swaps(fruits,n):
    # n = len(fruits)
    sortedFruits = sorted(fruits)
    
    # Create a mapping from fruit weight to its current index
    indices = {fruit: i for i, fruit in enumerate(fruits)}
    # print(indices)
    
    swaps = 0 

    for i in range(n):

        #if the current fruit is not in the correct position
        if fruits[i] != sortedFruits[i]:
            swaps += 1  
            correctFruit = sortedFruits[i]  # The correct fruit that should be at position i

            to_swap = indices[correctFruit]  # The index of where the correct fruit currently is
            
            # Update the indices dictionary to reflect the swap
            indices[fruits[i]] = to_swap
            indices[correctFruit] = i
            
            # Perform the swap in the fruits list
            fruits[i], fruits[to_swap] = fruits[to_swap], fruits[i]
    
    return swaps

n = int(input())
fruits = list(map(int, input().split()))
print(minimum_swaps(fruits,n))
