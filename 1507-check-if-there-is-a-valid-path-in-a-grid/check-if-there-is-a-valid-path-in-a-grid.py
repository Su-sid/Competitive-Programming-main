class Solution:
    def indexNotOutofRange(self, row, col, m, n):
        return (row >= 0 and row < m) and (col >= 0 and col < n)

    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        visited = [[False for j in range(n)] for i in range(m)]
        queue = []
        queue.append([0, 0])
        visited[0][0] = True
        streetObj = {
            #Each street has been and supporting possible next street has been put into objects 
            #Street[No]: (direction(index), ListofPossibleNextStreet)

            1: (([0, 1], [1, 3, 5]), ([0, -1], [1, 4, 6])),
            2: (([1, 0], [2, 5, 6]), ([-1, 0], [2, 3, 4])),
            3: (([1, 0], [2, 5, 6]), ([0, -1], [1, 4, 6])),
            4: (([1, 0], [2, 5, 6]), ([0, 1], [1, 3, 5])),
            5: (([0, -1], [1, 4, 6]), ([-1, 0], [2, 3, 4])),
            6: (([-1, 0], [2, 3, 4]), ([0, 1], [1, 3, 5]))
        }
        while queue:
            #While the queue is not empty, pop from the queue

            row, col = queue.pop(0)
            if row == m-1 and col == n-1: #index is at the end of the end of the, so return True
                return True
            for eachDir in streetObj[grid[row][col]]:
                #For direction of the current street, check possibleNextstreet
                #If there exist a possible nextStreet  notVisited, add it to the queue

                currRow = row + eachDir[0][0]
                currCol = col + eachDir[0][1]
                if self.indexNotOutofRange(currRow, currCol, m, n) and not visited[currRow][currCol]:
                    currStr = grid[currRow][currCol]
                    possibleStr = eachDir[1]
                    if currStr == possibleStr[0] or currStr == possibleStr[1] or currStr == possibleStr[2]:
                        queue.append([currRow, currCol])
                        visited[currRow][currCol] = True

        return False #If the queue become empty without getting to the end of the street
            





        