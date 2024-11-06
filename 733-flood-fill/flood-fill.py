class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        # visited=  [[False]*len(image[0])for _ in range(len(image))] 
        startColor = image[sr][sc]
        
        row= len(image)
        col=len(image[0])

        # print(startNode)
        def dfs(i,j , graph):
        #    chech out of bounds 
            if i< 0 or j < 0 or i >=row or j >= col:
                return 
        #   check of current pixel is same as starting color or if current pixel is same as new color[means it is already visited.]
            if graph[i][j] != startColor or graph[i][j] ==color : 
                return 

        # change current pixel color to new color
            graph[i][j]= color
        
        # perform the flood fill 
            dfs(i+1, j, graph) #down
            dfs(i-1, j, graph) #up 
            dfs(i, j+1, graph) #right 
            dfs(i, j-1, graph) #left

            # return graph

            

        dfs (sr, sc, image)
        # return dfs (sr, sc, image)
        return image

 