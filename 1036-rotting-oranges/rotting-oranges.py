class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0
        
        # Initialize the queue with all the rotten oranges
        # and count the number of fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1
        
        # Directions for moving up, down, left, right
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        minutes_passed = 0
        
        # BFS traversal
        while queue and fresh_count > 0:
            minutes_passed += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()
                
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh_count -= 1
                        queue.append((nx, ny))
        
        # If there are still fresh oranges left, return -1
        return minutes_passed if fresh_count == 0 else -1