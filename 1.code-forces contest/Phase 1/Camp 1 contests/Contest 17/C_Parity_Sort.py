

n= int(input())

def even(num):
    if num %2== 0:
        return True
    return False

for _ in range(n):
    length= int( input().strip())
    a= list(map(int, input().split()))

    # print(length)
    # print(nums)

    left=0
    right=left+1

    while left< length:
        while (right < length and 
        even(a[left]) == even(a[right]) and 
        a[left]> a[right]):
            # print(left,'--',right)
            # print(even(a[left]) ==  even(a[right]))
            # print(a[left] < a[right])
            a[left], a[right]= a[right], a[left]

            print(a[left],':-:', a[right])
            right+=1

        left+=1
    
        print('list',a)
       
    

   


        



        

    

    


