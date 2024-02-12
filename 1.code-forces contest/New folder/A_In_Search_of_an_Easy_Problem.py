def easy_problem( n, decisions):
    if 1<=n <= 100:
        if 1 in decisions:
            return "HARD"
        else:
            return "EASY"
    
n= int(input())
decisions = list(map(int, input().split()))

print(easy_problem(n, decisions))
