#take length of array
n = int(input())
arr = list(map(int, input().split()))

negative=list()
positive=list()
zero=list()

for i in arr:

    if i == 0:
        zero.append(i)
    elif i > 0:
        positive.append(i)

    else:
        negative.append(i)


if len(positive) == 0:
    for i in range(2):
        positive.append(negative.pop())

if len(negative) % 2 == 0:
    zero.append(negative.pop())

print(len(negative), *negative)
print(len(positive), *positive)
print(len(zero), *zero)