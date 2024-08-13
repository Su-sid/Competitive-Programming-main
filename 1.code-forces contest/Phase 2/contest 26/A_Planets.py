from collections import Counter
t= int(input())

results = []
for i in range(t):
    n, c = list(map(int, input().split()))
    planets= list(map(int, input().split()))


    orbit_count = Counter(planets)
  

    total_cost = 0

    for orbit, count in orbit_count.items():
        if count <= c:
            total_cost += count   
        else:
            total_cost += c 

    print(total_cost)

