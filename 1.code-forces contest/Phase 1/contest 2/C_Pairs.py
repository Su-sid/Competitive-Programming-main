n =int(input())

arr_a=list(map(int, input().split()))
arr_b=list(map(int, input().split()))
arr_c=list(map(int, input().split()))

#counting the fre of each element in the array a

frequency={}

for num in arr_a:
    frequency[num]= frequency.get(num, 0)+1


#counting each pair
    
possiblle_pairs= 0 
for j in range(n):
    possiblle_pairs+=frequency.get(arr_b[arr_c[j]-1],0)

print(possiblle_pairs)