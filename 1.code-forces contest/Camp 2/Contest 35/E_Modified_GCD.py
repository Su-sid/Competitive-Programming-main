def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

num1, num2= list(map(int, input().split()))

tests= int(input())
for _ in range(tests):

    low, high = list(map(int, input().split()))

    # result = gcd(num1, num2)
    result2 = gcd(low, high)
    
    # print(result)
    print(low, high)
    print(result2)