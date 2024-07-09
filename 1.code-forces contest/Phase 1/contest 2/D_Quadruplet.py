n,  target = list(map(int, input().split()))
#8   #15

int_values = list(map(int, input().split()))
#[3, 2, 5, 8,][ 1, 3, 2, 3]
#list starts from  index 1
#Print four integers: the positions of the values. 

def quadruplet(n, target, int_values):
    for i in range(n):
