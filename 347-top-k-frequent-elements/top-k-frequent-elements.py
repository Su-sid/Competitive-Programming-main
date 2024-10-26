class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    
        store = Counter(nums)

        sorted_store = sorted(store.items(), key=lambda x: x[1], reverse=True)

        final = [key for key, _ in sorted_store[:k]]

        return final
        