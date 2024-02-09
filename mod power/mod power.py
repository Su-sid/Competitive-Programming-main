# Enter your code here. Read input from STDIN. Print output to STDOUT


def find_mod_power(a: int, b: int, m: int)->list[int]:
    if 2<= m<= 1000:
        return [pow(a, b), pow(a, b, m)]

if __name__=='__main__':
    a=int(input())
    b=int(input())
    m=int(input())
    
    for n in find_mod_power(a, b, m):
        print(n)
    