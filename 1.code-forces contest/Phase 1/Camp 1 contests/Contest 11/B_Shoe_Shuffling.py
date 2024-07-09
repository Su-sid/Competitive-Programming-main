def solve(test_cases):
    results = []

    for n, s in test_cases:
        if n == 1:
            # With only one student, it's impossible to not give him his own shoes.
            results.append("-1")
            continue
        
        # Attempt to create a valid shuffling by rotating the indices
        # We rotate the array such that student i gets the shoes of student i+1,
        # and the last student gets the shoes of the first student.
        p = list(range(2, n + 1)) + [1]  # This is the rotation by one position

        # Check if this shuffle is valid
        valid = True
        for i in range(n):
            original_index = i
            new_shoes_index = p[i] - 1  # since p is 1-based
            if s[original_index] > s[new_shoes_index]:
                valid = False
                break
            if original_index == new_shoes_index:
                valid = False
                break
        
        if valid:
            results.append(" ".join(map(str, p)))
        else:
            # If the simple rotation does not work, check for any valid permutation
            found = False
            for i in range(n):
                if i != n - 1 and s[i] == s[i + 1]:
                    # There is a repeat, we can use a rotation trick
                    p = list(range(1, n + 1))
                    p[i], p[i + 1] = p[i + 1], p[i]  # Swap two similar sizes
                    if all(p[j] != j + 1 for j in range(n)):
                        results.append(" ".join(map(str, p)))
                        found = True
                        break
            if not found:
                results.append("-1")

    return results

# Example usage

test_cases= list()
tests = int(input())

for _ in range(tests):
    n= int(input())
    a = list(map(int, input().split()))

    test_cases.append([n,a])

output = solve(test_cases)
for line in output:
    print(line)



