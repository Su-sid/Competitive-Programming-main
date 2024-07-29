# tests=int(input())


# def removeSmaller():
#     n=int(input())
#     arr= list(map(int,input().split()))
#     # arr=arr[::-1]
  

#     for right in range(n-1,0,-1):
#         left=right-1
#         if arr[left]== arr[right] or abs(arr[right]-arr[left])== 1: 
#             # if  len(arr)> 0:
#             arr.pop()
#         else:
#             continue
              

#     if len(arr)==1:
#         return 'YES'
#     else:
#         return  'NO'
    


#     print(arr)


# # print(removeSmaller())


# for  i in range(tests):
#     print(removeSmaller())



def removeSmaller():
    n = int(input())
    arr = list(map(int, input().split()))
    
    arr.sort() 
    
    possible = True
    
    for i in range(n - 1):
        if arr[i + 1] - arr[i] <= 1:
            continue 
        else:
            possible = False
            break
    
    if possible:
        return 'YES'
    else:
        return 'NO'

tests = int(input())

for _ in range(tests):
    print(removeSmaller())
