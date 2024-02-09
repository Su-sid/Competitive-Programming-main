def loop_function(number: int)-> list[int]:
    squared_number=[]
    if 1 <= number <= 20:
        for n in range(number):
            squared_number.append(n**2)
    return squared_number

if __name__ == '__main__':
    n = int(input())
    output=loop_function(n)
    
    for x in output:
        print(x)