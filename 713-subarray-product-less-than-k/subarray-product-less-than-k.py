class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # sorted (nums)
        #[ 2, 5, 6, 10 ]

        right=left=result =0
        product=1
        
        # arr= list()
        length= len(nums)

        while right < length:
            product *= nums[right]
            
            while product >= k and  left <= right:
                product /= nums[left]
                left+=1
            result += right -left +1
            right+=1
        return result

