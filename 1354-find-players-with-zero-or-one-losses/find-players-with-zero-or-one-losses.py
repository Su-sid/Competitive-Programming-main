class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners= Counter()
        losers= Counter()
        for win, loss in matches:
            winners[win]+=1
            losers[loss]+=1

        # print(winners.keys())
        # print(losers.keys())

        wins= sorted(list(set(winners.keys())- set(losers.keys())))

        loss= sorted (list(k for  k, v in losers.items() if v == 1))

        return [wins, loss]
