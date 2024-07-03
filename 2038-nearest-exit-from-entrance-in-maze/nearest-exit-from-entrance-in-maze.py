class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  
        queue = deque([(entrance[0], entrance[1], 0)])  
        visited = set()
        visited.add((entrance[0], entrance[1]))

        while queue:
            x, y, steps = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited and maze[nx][ny] == '.':
                    if nx in {0, m-1} or ny in {0, n-1}:
                        return steps + 1
                    queue.append((nx, ny, steps + 1))
                    visited.add((nx, ny))
        
        return -1