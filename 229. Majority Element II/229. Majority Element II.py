from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count= Counter(nums)
        arr=set()
        for i in nums:
            if count[i]>len(nums)//3:
                arr.add(i)
        return arr

        