
n, m= list(map(int, input().split()))
names= list()
for _ in range(n):
    names.append(input())

if m == 0:
    print(n)
    for i in range(n):
        names.sort()
        print(names[i])
else:
    check= True
    for _ in range(m):
        rivals= list(map(str, input().split()))
    temp= list()

    for i in range(n):
        names.sort()

        if names[i] not in rivals:
            temp.append(names[i])
        if names[i] in rivals and check:
            temp.append(names[i])
            check= False

        else:
            check= True
            continue

    print(len(temp))
    for name in temp:
        print(name)

