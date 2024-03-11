from collections import defaultdict

test_cases= int(input())
results=[]
for _ in range(test_cases):

    lantern_count= int(input())
    max_point= 0
    a = defaultdict(list)

    for _ in range(lantern_count):
        a1,b1 = map(int, input().split())

        a[a1].append(b1)
    
    for i in sorted(a):
        j= 0
        turned_on_count= 0
        a[i].sort(reverse=True)

        while turned_on_count< i and j < len(a[i]):
            max_point += a[i][j]
            j+=1

            turned_on_count += 1
    results.append(max_point)

for result in results:
    print(result)