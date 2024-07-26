class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
        Scenario 1: (n+1)*(f-1) + X.
        Note: Where X is the frequency of occurrence of  the most frequent element.
        Final  scenario: max ( (n+1)*(f-1) + X, TotalJobs)
        '''
        TotalJobs= len(tasks)
        f=Counter(tasks).most_common()
        maxFreq= f[0][1]

        X= 0
        # Count number of occurence of  most frequent character.
        
        for element, freq in  f:
            if freq == maxFreq:
                X+=1
            else: 
                break
        

        return max ( (n+1)*(maxFreq-1) + X, TotalJobs)
