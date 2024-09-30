n = int(input())

nums= list( map(int, input().split()))

unique= len(set(nums))
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
print(factorial(unique))