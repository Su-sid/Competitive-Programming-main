from  itertools import accumulate

n, k= list(map(int, input().split()))
h= list(map(int, input().split()))

minimum= float('inf')
start_index = None

prefix=list(accumulate(h, initial=0))
# print(prefix)

for i in range(k, n+1):
    current_sum = prefix[i] - prefix[i-k]
   
    if current_sum < minimum:
        minimum = current_sum
        start_index = i - k +1
print(start_index)


