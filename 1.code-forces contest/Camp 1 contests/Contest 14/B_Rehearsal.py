# The first line of input contains n
#  (1≤n≤105)
# . Each of the next n
#  lines contains two integers x #  and y # , indicating that Maestro John has x
#  musicians each with a level of proficiency y
#  (1≤y≤109) # . The sum of the x
# 's is m #  (1≤m≤109 # ), the total number of musicians.


n = int(input())

mapping= {}
arr=[]

for _ in range(n):
    x, y = list(map(int, input().split()))

    for _ in range(x):
        arr.append(y)

# print(mapping)
print(arr)
current= float('inf')
j =0 
for i, num in enumerate(arr) :
    
    j=0 
    while j < len(arr):
        # print(j)
        # if i == j:
        #     continue
        # else:
        mapping[i]= min(num+arr[j], current)
        
        current=mapping[i]        
        j+=1
      
        
        # print(current)


# print(mapping)

    # for i in range(x):

        # print(i)
        # current= mapping[x] if x in mapping else float('inf')

        # if x in mapping:
        #     current= mapping
        # else: 
        #     current= float('inf')

        # print(mapping)
        # mapping[x]-min(current, abs(x-y))
    


    

   