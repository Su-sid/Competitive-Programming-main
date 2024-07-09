from itertools import combinations

n = int(input())
nums=list()
final= list()

for _ in range (n):
    num=int(input())
    nums.append(num)
    final.append(-(num))   

final.extend(nums)

comb= list( combinations(final, n))


def ans(comb):
    for i in comb:
        val=sum(i)
        if val == 0 or val ==360:
            return 'YES'
    return 'NO'   

print(ans(comb))

