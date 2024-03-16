class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
    #    right = len(nums)-1
    #    while 0 <right:
    #         for i in range(right):
    #             if nums[i]== nums[right]:
    #                 return nums[i]
    #         right-=1
        dictArr=dict()
   
        for i in nums:
            if i in dictArr:
                dictArr[i] +=1
            else:
                dictArr[i] = 1
        print(dictArr)
        for num, count in dictArr.items():
            if count >= 2:
                return num 
      




