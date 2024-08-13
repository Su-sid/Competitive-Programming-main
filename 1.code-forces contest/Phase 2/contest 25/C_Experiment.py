n=int(input())
experiments= []
for i in range(n):
    start, end, freq = list(map(int, input().split()))
    #create  tuples of two. 
    experiments.append((start, freq))
    experiments.append((end+1, -freq ))

experiments.sort()

# print(experiments)

max_rooms=0
cur_rooms=0
for _,change in experiments:
    cur_rooms+=change

    max_rooms=max(max_rooms,cur_rooms)
print(max_rooms)            