
t = int(input())
    
for _ in range(t):
    n = input().strip()
    memo = {}

    def dp(n, index , lastdigs, memo):
    
        if index == len(n):
            if lastdigs in {0, 25, 50, 75}:
                return 0
            else:
                return float('inf')
        
        if (index, lastdigs) in memo:
            return memo[(index, lastdigs)]
    
        steps = 1 + dp(n, index + 1, lastdigs, memo)
        
        current_digit = int(n[index])

        if lastdigs == -1:
            updated_lastdigs = current_digit

        elif lastdigs < 10:
            updated_lastdigs = lastdigs * 10 + current_digit
        else:
            updated_lastdigs = (lastdigs % 10) * 10 + current_digit
            
        keep_digit = dp(n, index + 1, updated_lastdigs, memo)
        
        result = min(steps, keep_digit)
        memo[(index, lastdigs)] = result
        return result

    result = dp(n, 0, -1, memo)
    print(result)
