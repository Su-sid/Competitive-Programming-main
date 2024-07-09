test_cases= int(input())
list_s= list(map(str, input().split()))

target= ['abc', 'acb','bac', 'cba']

def simon_sort( list_s):
    for s in list_s:
        if s in target:
            return print('YES')
        
        return print('NO')

   