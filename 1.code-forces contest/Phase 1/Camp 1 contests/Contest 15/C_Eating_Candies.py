test= int(input())

for _ in range(test):
    n = int(input())
    arr=list(map(int,input().split()))
  

    alice, bob= 0, n-1
    alicetotal=0
    bobtotal=0
    total=0

    while alice <= bob:
    
        if alicetotal < bobtotal:
            alicetotal +=arr[alice]
            alice+=1
        else:
            bobtotal +=arr[bob]
            bob-=1
        if bobtotal==alicetotal:
            total=alice+ n-bob-1
        # total.append([arr[alice],arr[bob]])
    print(total)

