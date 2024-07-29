import heapq as hp


n=int(input())
potions= list(map(int,input().split()))

# arr.sort(reverse=True)

health = 0
potionsDrunk= 0
heap= []
# consume potions and maintain health at above 0
for p in potions :
    health+=p
    hp.heappush(heap, p)
    potionsDrunk+=1

    if health < 0 :
        health -=hp.heappop(heap)
        potionsDrunk-=1
# return the total potions Drunk 
print(potionsDrunk)