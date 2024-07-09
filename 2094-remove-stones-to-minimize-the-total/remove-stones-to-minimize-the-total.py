class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        negativePiles = [-p for p in piles]
        total = sum(piles)
        heapq.heapify(negativePiles)
        for _ in range(k):
            maxi = heapq.heappop(negativePiles)
            decrement = math.floor(-maxi / 2)
            total -= decrement
            heapq.heappush(negativePiles, maxi + decrement)
            
        return total