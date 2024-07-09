
def yogurt_sale(n,a ,b):

    remainder= n% 2

    original_price= n* a
    discount_price= int((((n- remainder)/2)*b)+(remainder*a))

    final_price= min(original_price, discount_price)
    # print()

    return final_price


tests = int(input())


for _ in range(tests):
    n, a, b = list(map(int, input().split()))

    print(yogurt_sale(n,a,b))