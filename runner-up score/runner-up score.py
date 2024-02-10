def runner_up(number_scores: int, arr: list[int])-> int:
    # arr.sorted(reverse=True)
    for i in range(number_scores):
        if not arr[0]==arr[i]:
            return arr[i]

if __name__ == '__main__':
    n = int(input())
    arr = sorted(map(int, input().split()), reverse=True)
    
    print(runner_up(n, arr))