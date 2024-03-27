class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n_2 = len(skill) // 2
        sum_ = sum(skill)
        if sum_ % n_2 != 0:
            return -1
        team = sum_ // n_2
        
        chemistry = 0
        skill.sort()
        for i in range(n_2):
            a = skill[i]
            b = skill[-i - 1]
            if a + b != team:
                return -1
            chemistry += a * b
        return chemistry