

# # t = int(input())

# # results = []

# # for _ in range(t):
    
# #     n, k = list(map(int, input().split()))
    
# #     picks = list(map(int, input().split())) #[10, 10, 3, 3]
   
# #     memo = [[-1 ]*2 for _ in range(n)]
# #     print(memo)
    
# #     def dp(i, half_picked):
# #         if i >= n:
# #             return 0
        
# #         if memo[i][half_picked] != -1:
# #             return memo[i][half_picked]
        
# #         # if picks[i]> k: 
# #         full_pick = (picks[i] - k) + dp(i + 1, half_picked)
# #         # else:
# #             # full_pick-= k -picks[i] + dp(i + 1, half_picked)



# #         print(full_pick)
        
# #         half_pick = float('-inf')
# #         if not half_picked:
# #             half_pick = (picks[i] // 2) + dp(i + 1, True)
        
# #         memo[i][half_picked] = max(full_pick, half_pick)
# #         return memo[i][half_picked]
    
   
# #     print(dp(0, 0))


# def solve():

#     t = int(input())

#     for _ in range(t):
       
#         n, k = list(map(int, input().split()))
        
#         produce = list(map(int, input().split()))
        
 
#         memo = [[-1 for _ in range(2)] for _ in range(n)]
        
#         def dp(i, half_picked, n, k, produce):
#             if i >= n:
#                 return 0
#             if memo[i][half_picked] != -1:
#                 return memo[i][half_picked]
            
     
#             if produce[i] >= k:
#                 full_pick = (produce[i] - k) + dp(i + 1, half_picked, n, k, produce)
#                 print(full_pick)
#             else:
#                 full_pick = -(k - produce[i]) + dp(i + 1, half_picked, n, k, produce)
        
#             half_pick = float('-inf')
#             if not half_picked:
#                 future_half_picked_points = dp(i + 1, True, n, k, produce)
#                 half_pick = (produce[i] // 2) + future_half_picked_points
            
#             memo[i][half_picked] = max(full_pick, half_pick)
#             return memo[i][half_picked]
#         dp(0, 0, n, k, produce)
        
#         # Start the DP from the first tree with no trees half-picked yet
#         # print(dp(0, 0, n, k, produce))
    
#     # Output the results for all test cases
#     # print('\n'.join(map(str, results)))


def solve():
    # Read number of test cases
    t = int(input())
    
    results = []
    
    for _ in range(t):
        # Read n (number of trees) and k (magic number)
        n, k = list(map(int, input().split()))
        
        # Read produce list for the current test case
        produce = sorted(list(map(int, input().split())), reverse=True)
        
        total_points = 0
        half_pick_made = False
        
        for i in range(n):
            if half_pick_made:
                # Fruits are halved if a half pick was made previously
                produce[i] //= 2
            
            # Calculate points for full pick
            full_pick_points = produce[i] - k
            
            # Calculate points for half pick
            half_pick_points = produce[i] // 2
            
            # Decide to use Full Pick or Half Pick
            if not half_pick_made and half_pick_points > full_pick_points:
                # Half Pick gives more points and we haven't picked it before
                total_points += half_pick_points
                half_pick_made = True
            else:
                # Full Pick or continue picking full after a Half Pick
                total_points += full_pick_points
        
        results.append(total_points)
    
    # Output the results for all test cases
    print('\n'.join(map(str, results)))


solve()