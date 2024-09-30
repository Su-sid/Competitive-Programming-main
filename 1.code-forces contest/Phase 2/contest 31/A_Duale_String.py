# iterate the test cases 
for _ in range (int(input())):

    str= input()

    n= len(str)
    final= True

    # special case when len == 1
    if n%2!=0:
        final = False
        # break

    # Traverse half the length of the string 
    else:
        for i in range(n//2):
            # print(str[i], str[n//2+i])
            if str[i]!=str[n//2+i]:

                final = False
                break

    if final:
        print('YES')
    else:
        print('NO')



