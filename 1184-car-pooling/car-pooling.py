class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # O(n)

        #form the prefix array
        prefixarr= [0]*1001
        # add the passengers at start and delete at end 
        for t in trips:
            passengers, start, end= t
            prefixarr[start]+= passengers
            prefixarr[end]-=passengers 

        #store the total number of passengers
        totalpass=0
        #go over the entire array in one pass and get the total passengers. 
        for i in range( 1001):
            totalpass+= prefixarr[i]
            #
            if totalpass> capacity:
                return False 
        return True




        # #O(n log n) 
        # trips= sorted(trips, key=lambda a: a[1])
        # minHeap= []
        # curPass=0

        # for numPass, start, end in trips:            
        #     while minHeap and minHeap[0][0]<= start:
        #         curPass-=minHeap[0][1]
        #         heapq.heappop(minHeap)

        #     curPass +=numPass
        #     if curPass> capacity:
        #         return False
        #     heapq.heappush(minHeap, [start, numPass])
        # return True
