
n= int(input())
words = [input () for _ in range(n)]
for word in words:
    if word== word[::-1]:
        print(0)
    else:
        changes= 0
        length= len(word)//2
        for i in range(length):
            if word[i]!= word[-i-1]:
                changes+=1
        print(changes)
