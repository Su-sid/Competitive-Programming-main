"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph = dict ()
        for employee in employees:
            graph[ employee.id]= employee

        def dfs(id):
            totalImportance=graph[id].importance
            for neighbor in graph[id].subordinates:
                totalImportance+= dfs(neighbor)
            return totalImportance

        return dfs(id)