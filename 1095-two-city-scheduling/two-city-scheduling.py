class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:

        costs.sort( key=lambda cost: cost[0] - cost[1] )
        n = len(costs)//2
        total =0 

        for i, cost in enumerate(costs):
            if i < n:
                total +=cost[0]
            else:
                total+=cost[1]
        return total




