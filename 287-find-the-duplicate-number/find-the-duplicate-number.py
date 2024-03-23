class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dictArr=Counter(nums)
        for num, count in dictArr.items():
            # print(element)
            if count>1:
                return num 