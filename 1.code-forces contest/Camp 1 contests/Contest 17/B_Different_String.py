

n= int(input())

for _ in range(n):
    string= input().strip()
    length= len(string)
   

    if string == string[::-1] or length< 1:
        print('NO')
    else:
        print('YES')
        mid= len(string)//2
        left, right= string[:mid], string[mid:]

        print(right+left)


