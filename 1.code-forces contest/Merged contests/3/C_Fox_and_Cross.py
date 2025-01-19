
def valid_cross(grid, r, c, n, visited):
    
    cross = [
        (0, 0),   # MID
        (-1, 0),  # UP
        (1, 0),   # DOWN
        (0, -1),  # L
        (0, 1)    # R
    ]
    
    can_form = True
    temp_visited = set()  
    # c -- For COLUMN and r -- For ROW
    for dr, dc in cross:
        nr, nc = r + dr, c + dc
        cell_pos = (nr, nc)
        
        if (nr < 0 or nr >= n or nc < 0 or nc >= n or 
            grid[nr][nc] != '#' or cell_pos in temp_visited or 
            visited[nr][nc]):
            can_form = False
            break
        temp_visited.add(cell_pos)
    
    if can_form:
        for dr, dc in cross:
            visited[r + dr][c + dc] = True
    
    return can_form

def dfs():
    n = int(input())
    grid = [list(input()) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    
    total_hash = sum(row.count('#') for row in grid)
    
    if total_hash % 5 != 0:
        return "NO"
    
    found_cross = True
    while found_cross:
        found_cross = False
        for i in range(n):
            for j in range(n):
                if grid[i][j] == '#' and not visited[i][j]:
                    if valid_cross(grid, i, j, n, visited):
                        found_cross = True
                        break
            if found_cross:
                break
    
    for i in range(n):
        for j in range(n):
            if grid[i][j] == '#' and not visited[i][j]:
                return "NO"
    
    return "YES"

print(dfs())