round= int(input())
for _ in range(round):
    n,k = list(map(int, input().split()))
    nums= sorted(list(map(int, input().split())))


    left=2
    right=-1

    if k==1:
        print(sum(nums[left:]))
    if k==2:
        right-=1
        print(sum(nums[left:right+1]))
