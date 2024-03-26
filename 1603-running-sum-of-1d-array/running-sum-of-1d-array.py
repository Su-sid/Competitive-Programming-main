class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # pref=[0]
        
        pref=[0]*(len(nums)+1)

        for i in range(1, len(nums)+1): 
            # print(i)
            pref[i]=pref[i-1]+ nums[i-1]
        return pref[1:]


        