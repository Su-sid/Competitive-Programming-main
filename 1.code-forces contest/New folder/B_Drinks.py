 

'''
variable 
a =the number of drinks in the fridge

drink_ratios= the ratio of orange in each drink


output 

the average of the drink_ratio/ a
'''
def b_drinks( n:int, drink_ratio:list[int])->float:

    total=int(0)
    for i in range(n):
        total+=drink_ratio[i]

        average= total/n
    return average
    # return round(total/n,12)




n = int(input())
drink_ratio = list(map(int, input().split()))
result= b_drinks(n, drink_ratio)
print(f"{result:.12f}")
