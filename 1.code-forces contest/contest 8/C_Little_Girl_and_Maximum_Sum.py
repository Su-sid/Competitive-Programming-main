n, q = map(int,input().split())

array =list(map(int,input().split()))

prefix_array = [0] * (n + 1)

for _ in range(q):
    l, r = map(int, input().split())
    # Dont forget our input is I-indexed
    prefix_array[l - 1] += 1
    prefix_array[r] -= 1

    # Calculate the prefix sum

for i in range(1, n):
   prefix_array[i]+= prefix_array[i-1]

# Remove the Last element
prefix_array.pop()
array.sort()
prefix_array.sort()
# Calculate the sum
sum =sum( [array[i] * prefix_array[i] for i in range(n)])
print(sum)