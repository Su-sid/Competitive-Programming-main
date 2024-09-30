
for _ in range(int(input())):
    x = int(input())

    if x ==1:
        print(x+2)
    elif x & (x - 1) == 0:
        print(x +1)
    else:
   
        print(x & -x)

