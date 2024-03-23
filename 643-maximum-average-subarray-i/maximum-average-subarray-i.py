class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # right, left,length= 0, 0, len(nums)-1
        
        window_sum= sum(nums[:k])
        max_sum =window_sum/k
        for i in range(k,len(nums)):
            window_sum+=nums[i]
            window_sum-=nums[i-k]
            max_sum=max(max_sum, window_sum/k)  
        return max_sum