# arr = list(map(int,input().split()))
a= input().strip()
arr=sorted(list(map(int,a)))
b= int(input())
left = 0

if arr[0]==0 and len(arr)>1:
    right= 1
    while   arr[right]== 0 :
        right+=1
    left=arr[right]

    arr[0],arr[1]=left,arr[0]

val=''.join(map(str,arr))

print('OK' if int(val)==b else 'WRONG_ANSWER')
