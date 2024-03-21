class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left=result =0
        product=1

        length= len(nums)
        for right in range( length):
            product *= nums[right]
        #repeat reducing product until it matches K 
            while product >= k and  left <= right:
                product /= nums[left]
                left+=1
            result += right -left +1
            # right+=1
        return result

