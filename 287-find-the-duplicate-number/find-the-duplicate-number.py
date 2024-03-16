class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # dictArr=dict()
        # for i in nums:
        #     if i in dictArr:
        #         dictArr[i] +=1
        #     else:
        #         dictArr[i] = 1
        # print(dictArr)
        dictArr=Counter(nums)
        for num, count in dictArr.items():
            # print(element)
            if count>1:
                return num 