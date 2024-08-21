class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix[0])
        # dp = [[0]*n for _ in range(n)]
        
        for row in range(1, n):
            for col in range(n):
                left= matrix [row -1 ] [col-1] if col > 0 else float('inf') 
                right = matrix [row -1 ] [col+1] if col < n-1 else float('inf') 
                middle= matrix [row -1 ] [col] 

                matrix[row][col]=  matrix[row][col]+ min(left, right, middle)

        return min(matrix[-1])

