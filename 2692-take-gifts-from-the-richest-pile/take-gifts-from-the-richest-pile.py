
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for _ in range(k):
            # Find the index of the pile with the maximum number of gifts
            max_index = gifts.index(max(gifts))
            
            # Replace the pile with the floor of the square root of its current value
            gifts[max_index] = math.floor(math.sqrt(gifts[max_index]))

        # Return the sum of all remaining gifts
        return sum(gifts)