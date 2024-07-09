n= int(input())
arr= list(map(int, input().split()))

def create_permutation(arr):
    if len(set(arr)) == 1:
        return "-1"
    arr.sort()
    return " ".join(map(str, arr))

print(create_permutation(arr))