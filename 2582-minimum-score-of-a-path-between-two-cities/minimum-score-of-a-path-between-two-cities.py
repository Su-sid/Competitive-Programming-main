class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        dp=list(range(n+1))

        def find(x):
            if dp[x]!=x:dp[x]=find(dp[x])
            return dp[x]
        
        cost=collections.defaultdict(lambda: float('inf'))
        
        for i,j,k in roads:  
            i,j=find(i),find(j)                    
            cost[j]=min([cost[j],cost[i],k])
            dp[i]=dp[j]
                
        return cost[find(1)]