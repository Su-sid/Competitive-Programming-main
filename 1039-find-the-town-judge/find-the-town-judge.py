class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        result = list()
        store= set()
        store2= set()
        
        for fro, to in trust:
            
            store.add(fro)
            store2.add(to)
        temp= store2 - store


        if len(temp)!=1:
            return -1
        # if n == 1:
        #     return 1
            
        judge_candidate = temp.pop()

        count = 0
        for fro, to in trust:
            if to == judge_candidate:
                count += 1

        return judge_candidate if count == n - 1 else -1
