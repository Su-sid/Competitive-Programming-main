t= int(input())
origin= 'codeforces'


for _ in range(t):
    count=0

    s= input()

    for char in range(10):
        if s[char]!= origin[char]:
            count+=1
    
    print(count)

