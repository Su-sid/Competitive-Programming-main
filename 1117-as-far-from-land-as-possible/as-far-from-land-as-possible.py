class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
       
        row, col = len(grid), len(grid[0])
        queue = deque((i,j) for i in range(row) for j in range(col) if grid [i][j]  )  
         
        ans=-1
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] 

        def boundChecker(nx, ny):
            return 0 <= nx < row and 0 <= ny < col
            
        if len(queue) in (0, row * row):
            return ans      

        while queue:
            ans+=1
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    
                    if boundChecker(nx,ny) and grid[nx][ny] == 0:
                        grid[nx][ny]=1 
                        queue.append((nx, ny))
        return ans