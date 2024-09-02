class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # minimum min initializing a value to float(inf)
        # row, col= len(grid), len(grid[0])

        # memo= [ [float('inf')]*(col+1) for _ in range(row+1)]
        # memo[row-1][col]=0

        # for r in range(row-1,-1,-1):
        #     for c in range(col-1,-1,-1):
        #         memo[r][c]= grid[r][c] + min(memo[r-1][c],memo[r][c-1])

        # return memo[0][0]

        # consume the lengths of the rows -> n and columns -> m

        m = len(grid)
        n = len(grid[0])

        # define recursive dp functions that takes the arguments: i and j -> 
                
        # def dp(i,j):
        #     # check out of bound condition if reached return
        #     if i >= m or j>=n:
        #         return float('inf')
            
        #     if i == m-1 and j == n-1:
        #         return grid[i][j]
            
        #     return grid[i][j] + min(dp(i+1,j), dp(i,j+1))
            
        
        # return dp(0,0)


        m = len(grid)
        n = len(grid[0])
        
        cache = {}
        
        def helper(i,j):
            if i >= m or j>=n:
                return float('inf')
            
            if i == m-1 and j == n-1:
                return grid[i][j]
            
			# return from cache if present
            if (i,j) in cache :
                return cache[(i,j)]
			
			# populate cache
            cache[(i,j)] = grid[i][j] + min(helper(i+1,j), helper(i,j+1))
            return cache[(i,j)]
            
        return helper(0,0)