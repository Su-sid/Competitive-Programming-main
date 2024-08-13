class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order = []
        inDegree = [0] * numCourses
        graph = {i: [] for i in range(numCourses)}
        # Initialize the graph
        for target, pre in prerequisites:
            graph[pre].append(target)
            inDegree[target] += 1
        
        # Find all courses with no prerequisites
        queue = [i for i in range(numCourses) if inDegree[i] == 0]
        
        # Process each course
        while queue:
            node = queue.pop()
            order.append(node)
            
            for neighbor in graph[node]:
                inDegree[neighbor] -= 1
                if inDegree[neighbor] == 0:
                    queue.append(neighbor)
        
        return order if len(order) == numCourses else []