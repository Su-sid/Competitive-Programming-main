n= int(input())
arr= list(map(int, input().split()))

arr.sort()
wait= 0 
pitstop= 0

for i, num in enumerate(arr):

    if wait <= num:
        pitstop+=1
        wait+= num

print(pitstop)
