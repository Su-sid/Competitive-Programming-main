class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        # will calculate result in specific time
        self.resultAtTimes = {}
        self.times = times
        storeFrequence = Counter()
        n = len(persons)
        currMax = 0
        personMax = 0
        for i in range(n):
            storeFrequence[persons[i]] += 1
            if storeFrequence[persons[i]] >= currMax:
                currMax = storeFrequence[persons[i]]
                personMax = persons[i]
            self.resultAtTimes[times[i]] = personMax
    def q(self, t: int) -> int:
        timeMostRelative = 0
        left = 0
        right = len(self.times) - 1
        if t in self.resultAtTimes: return self.resultAtTimes[t]
        while left <= right:
            mid = (left + right) // 2
            if self.times[mid] <= t:
                timeMostRelative = self.times[mid]
                left = mid + 1
            else:
                right = mid - 1
        return self.resultAtTimes[timeMostRelative]

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)

# class TopVotedCandidate:

#     def __init__(self, persons: List[int], times: List[int]):
     
#         self.times= times
#         self.persons= persons

#     def search( self, arr, target):

#         left, right= 0, len(arr)-1
#         while left <= right:
#             mid = left + (right- left)//2
           
#             if arr[mid] > target:
               
#                 right = mid-1
                
#             elif arr[mid]<= target:

#                 left= mid+1 
               
#         return right
               
#     # find = search([0,6,39,52,75], 99)

#     # print('{',find)

#     def q(self, t: int) -> int:
       
#         find = self.search(self.times,t)
     
#         if t > self.times[-1]:
#             return 0
#         else:
#             return self.persons[find]

# # Your TopVotedCandidate object will be instantiated and called as such:
# # obj = TopVotedCandidate(persons, times)
# # param_1 = obj.q(t)