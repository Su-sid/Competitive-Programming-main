class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:

        x_points = sorted([point[0] for point in points])

        print(x_points)
        output= list()
        for pnt in range(1, len(x_points)):
            output.append(x_points[pnt]-x_points[pnt-1])
        
        return max(output)
            

     


        