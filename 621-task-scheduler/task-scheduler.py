class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        # where X is the frequency of occurrence of  the most frequent element.
        TotalJobs= len(tasks)
        f=Counter(tasks).most_common()
        maxFreq= f[0][1]

        X= 0
        for element, freq in  f:
            if freq == maxFreq:
                X+=1
        
        # print(maxFreq)
        # print(X)

        # print(f)

        return max ( (n+1)*(maxFreq-1) + X, TotalJobs)

        '''
        (n+1)*(f-1) + X.

        max ( (n+1)*(f-1) + X, TotalJobs)
        '''