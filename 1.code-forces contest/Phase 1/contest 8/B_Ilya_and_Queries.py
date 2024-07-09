s= input ()
q= int(input ())

queries=[]
for _ in range(q):
    li,ri= list(map(int, input().split()))
    queries.append([li,ri])

n = len(s)
prefix_counts = [0] * n

for i in range(1, n):
    if s[i] == s[i-1]:
        prefix_counts[i] = prefix_counts[i-1] + 1
    else:
        prefix_counts[i] = prefix_counts[i-1]

for li, ri in queries:
    answers= prefix_counts[ri - 1] - prefix_counts[li - 1]
    print(answers)