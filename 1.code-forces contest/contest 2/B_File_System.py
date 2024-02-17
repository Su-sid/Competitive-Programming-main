n = int(input().strip())

request_list=[]

for _ in range(n):
    

    request= input()
    
    if not request in request_list: 
        request_list.append(request)
        print('OK')
    elif request in request_list:
        value=1
        if  not int(request[-1])== value:
            print(request+str(value))
        value+=1
