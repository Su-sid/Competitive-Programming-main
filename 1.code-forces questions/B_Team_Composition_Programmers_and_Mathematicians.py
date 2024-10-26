for _ in range(int(input())):
    a, b = list (map(int, input().split()))

    ans = min ( min(a, b), (a+b)//4)

    print(ans)
    
    
    


        