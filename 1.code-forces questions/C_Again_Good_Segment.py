from collections import defaultdict

n, k = map(int, input().split())  
arr = list(map(int, input().split()))  

count =0
hashmap= defaultdict(int)#{}
left =0

for i in range(n):

    hashmap[arr[i]]+=1
    while hashmap and hashmap[arr[i]] >= k:
        count+= n - i
        hashmap[arr[left]]-= 1
        if hashmap[arr[left]]==0: 
            del hashmap[arr[left]] 
        left +=1
print (count)