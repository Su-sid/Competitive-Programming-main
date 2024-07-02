class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        visited=set()
   

        def dfs(key):
            if key in visited:
                return

            visited.add(key)

            for k in rooms[key]:
                dfs(k)
        dfs(0)
        return len(rooms)== len (visited)
            
            



