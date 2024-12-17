n, a, b = map(int, input().split())
if b == 0:
    print(a)
final_entrance = (a + b) % n 

if final_entrance == 0: 
    final_entrance = n

print( final_entrance)
