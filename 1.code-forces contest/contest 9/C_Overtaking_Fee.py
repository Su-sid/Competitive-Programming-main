n = int(input())
enter = list(map(int, input().split()))
exit = list(map(int, input().split()))

carhash = {car: i for i, car in enumerate(exit)}
count = 0
end = -1

for car in enter:
    if carhash[car] > end:
        end = carhash[car]
    else:
        count += 1

print(count)

