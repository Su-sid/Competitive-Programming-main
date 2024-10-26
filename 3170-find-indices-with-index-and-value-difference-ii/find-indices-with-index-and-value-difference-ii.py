class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        maxIndex, minIndex= 0,0
        for right in range(indexDifference, len(nums)):

            left = right- indexDifference
            if nums[left] < nums[minIndex]:
                minIndex= left#1- i
                # ndexDifference

            if nums[left]> nums[maxIndex]:
                maxIndex= left

            if abs(nums[right]- nums[minIndex])>= valueDifference:
                return [minIndex, right]
            if abs(nums[right]- nums[maxIndex])>= valueDifference:
                return [maxIndex, right]

        return [-1,-1]

