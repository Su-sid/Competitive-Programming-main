import heapq as hq
tests = int(input())
for _ in range(tests):
    n= int(input())
    arr= list(map(int, input().split()))
    sump = 0 
    stored = []

    for card in arr:
       
        if card==0 :
           
            if stored:
             
                sump +=-hq.heappop(stored)
        else: 
            hq.heappush(stored, -card)
    print(sump)
