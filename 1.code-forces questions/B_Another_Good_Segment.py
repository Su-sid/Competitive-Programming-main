n, s = map(int, input().split())  
a = list(map(int, input().split()))  
segments = 0
l =r = 0
count = {}  

while r < n:
    if a[r] in count:
        count[a[r]] += 1
    else:
        count[a[r]] = 1
    while len(count) > s:
        count[a[l]] -= 1
        if count[a[l]] == 0:
            del count[a[l]]
        l += 1
    segments += r - l + 1
    r+=1
print(segments)
