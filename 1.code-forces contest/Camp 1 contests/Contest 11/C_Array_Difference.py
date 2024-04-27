
def maximize_difference(test_cases):
    results = []
    for n, m, a, b in test_cases:
        # Sort both arrays
        a.sort()
        b.sort()
        
        # Maximum difference computation
        max_diff = 0
        for ai in a:
            # Compute the maximum difference by comparing with smallest and largest element in b
            diff_with_smallest = abs(ai - b[0])
            diff_with_largest = abs(ai - b[-1])
            max_diff += max(diff_with_smallest, diff_with_largest)
        
        print(max_diff)
    


test_cases= list()
tests = int(input())

for _ in range(tests):
    n,m = list(map(int, input().split()))

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    test_cases.append([n,m,a,b])


# Calculate the results using the defined function
print( maximize_difference(test_cases))

# print(test_cases)