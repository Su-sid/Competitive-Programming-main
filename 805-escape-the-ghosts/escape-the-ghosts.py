class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        a=abs(target[0])+abs(target[1])
        for i ,j in ghosts:
            b=abs(target[0]-i)+abs(target[1]-j)
            if b<=a:
                return False
        return True