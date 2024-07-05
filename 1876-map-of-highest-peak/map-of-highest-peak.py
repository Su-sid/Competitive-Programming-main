class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
               
        row, col = len(isWater), len(isWater[0])
        queue = deque( )  

        ans=[[-1]*col for _ in range(row)]
        # print(ans)    

        # Build the ans matrix to store visited cells.
        for i in range(row):
            for j in range(col):
                if  isWater [i][j]==1:
                    queue.append([i,j])
                    ans[i][j]=0
        # print(queue)  
        # print(ans)  
          
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] 

        def boundChecker(nx, ny):
            return 0 <= nx < row and 0 <= ny < col
        #  Do BFS ON THE QUEUE
        while queue:
          
            for _ in range(len(queue)):
                x, y = queue.popleft()

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy

                    if boundChecker(nx,ny) and ans[nx][ny] == -1:
                        ans[nx][ny]=ans[x][y]+1 
                        queue.append((nx, ny))
        return ans