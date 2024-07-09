def can_reach_target(n, portals, target):

    current = 1
    visited = set()
    
    while current <= n:
        if current == target:
            return True
        visited.add(current)
        
        if current - 1 < len(portals):
            next_cell = current + portals[current - 1]
        else:
            return False
        
    
        if next_cell in visited or current >= n:
            return False
   
        current = next_cell

    return False

n , target=  list(map(int, input().split())) 
portals = list(map(int, input().split()))


print('YES' if can_reach_target(n, portals, target) else 'NO')
