class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:

        graph = defaultdict(list)

        for arr in edges:
            fro, to = arr
            graph[fro].append(to)
            graph[to].append(fro)

        stack = [source]
        visited = set()

        while stack:
            current = stack.pop()

            if current == destination:
                return True

            if current not in visited:
                visited.add(current)

                for neighbor in graph[current]:

                    if neighbor not in visited:
                        stack.append(neighbor)

        return False
