# # from itertools import zip_longest
# class Solution:
#     def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
#         heap =[]

#         seq=[]
#         if len(nums1)==0  and len(nums2) == 0:
#             return []

#         for i in range(min(k, len(nums1))):
#             for j in range(min (k, len(nums2))):
#                 pair = [nums1[i],nums2[j]]
#                 sumpair = nums1[i]+nums2[j]
#                 # for j in nums2:
#                 heappush(heap, (-(sumpair), pair))

#                 if sumpair > -heap[0][0]:
#                     break

#                 if len(heap)>k:
#                     heappop(heap)

#         return ([arr for pos, arr in heap ])

class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        resV = []  # Result list to store the pairs
        pq = []  # Priority queue to store pairs with smallest sums, sorted by the sum

        # Push the initial pairs into the priority queue
        for x in nums1:
            heapq.heappush(pq, [x + nums2[0], 0])  # The sum and the index of the second element in nums2

        # Pop the k smallest pairs from the priority queue
        while k > 0 and pq:
            pair = heapq.heappop(pq)
            s, pos = pair[0], pair[1]  # Get the smallest sum and the index of the second element in nums2

            resV.append([s - nums2[pos], nums2[pos]])  # Add the pair to the result list

            # If there are more elements in nums2, push the next pair into the priority queue
            if pos + 1 < len(nums2):
                heapq.heappush(pq, [s - nums2[pos] + nums2[pos + 1], pos + 1])

            k -= 1  # Decrement k

        return resV  # Return the k smallest pairs