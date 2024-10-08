class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        memo = defaultdict(int)

        def inbound(row,col):
            return 0 <= row and row < n and 0 <= col and col < m and not obstacleGrid[row][col]
        def dp(row,col):

            if not inbound(row,col):
                return 0
            
            if row == n-1 and col == m-1:
                return 1
            
            if (row,col) not in memo:
                memo[(row,col)] = dp(row+1,col) + dp(row,col+1)
            
            return memo[(row,col)]
        
        return dp(0,0)