t= int (input ( ) )

for _ in range(t):
    n =int (input ( ))
    c= list( map( int, input().split()))
    
    c.sort()
    possible = True
    sumA = 1

    if c[0] !=1:
        possible =False

    for i in range (1, len (c)):
        if c [i] > sumA:
            possible = False
            break
        sumA += c [i]

    if possible:
        print ("YES")
    else:
        print ("NO")
        # sorted(list(), )