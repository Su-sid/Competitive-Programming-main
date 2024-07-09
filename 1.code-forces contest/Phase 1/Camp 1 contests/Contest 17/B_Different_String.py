n= int(input())

for _ in range(n):
    string= input().strip()
    # length= len(string)
   

    if len(set(string)) == 1:
        print('NO')
    else:
        print('YES')
        string = list(string)  # Convert to list to make swaps easier
        for i in range(1, len(string)):
            if string[i] != string[0]:
                string[0], string[i] = string[i], string[0]
                # break

        print("".join(string))
        # print(string)


