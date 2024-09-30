for _ in range( int(input())):
    length= int(input())

    arr= list( map(int, input().split()))

    left, right, suitable_pairs = 0, 0, 0

    # for i, right in enumerate(arr):
    #     while left < length and right< (i - left +1):
    #         left+=1

    #     suitable_pairs+= (i -left +1)

    # print(suitable_pairs) 
        
    # for i in range(1, length):#(int i=1  i<=n  i++)
    #     # {   
    #         # int left=i,right=n,search=i
        
    #     while right >= left:
    #         # {
    #             mid = right-(right-left)//2
    #             if (query(i , mid) + i-1 >= 0) 
    #                 # {
    #                 search = mid 
    #                 left = mid+1 
    #                 continue
    #                 # } 
    #             right = mid-1
                
    #         # }
    # ANS += search-i+1
    # # }
    # print(suitable_pairs)