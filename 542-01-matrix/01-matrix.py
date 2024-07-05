class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row, col = len(mat), len(mat[0])
        queue = deque()  
         
        ans=mat.copy()
        #create the ans matrix

        for i in range(row):
            for j in range(col):
                if ans[i][j]== 0:
                   queue.append((i,j))
                   continue
                ans[i][j]=-1 
        print(ans)
        # print(queue)

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] #back,down,up,front 

        def boundChecker(nx, ny):
            return 0 <= nx < row and 0 <= ny < col


        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if boundChecker(nx,ny) and ans[nx][ny] == -1:
                    ans[nx][ny]=ans[x][y] +1    
                    queue.append((nx, ny))
              
        return ans