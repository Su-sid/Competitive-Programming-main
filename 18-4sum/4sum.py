class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        n =  len(nums)
        nums.sort()
        solution = set()
        
        for i in range(n):
            for j in range(i+1, n-1):
                l = j + 1
                r = n-1
                while r > l:
                    sum_ = nums[i] + nums[j] + nums[l] + nums[r]
                    if sum_ == target:
                        solution.add((nums[i], nums[j], nums[l], nums[r]))
                        l += 1
                    elif sum_ > target:
                        r -= 1
                    else:
                        l += 1
        return solution
