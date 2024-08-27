class Solution:

    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        n=len(nums)
        cnt=0
        def binarysearch(nums,val):
            left,right=0,len(nums)-1

            while left<=right:
                mid= left+(right- left)//2

                if nums[mid]==val:
                    return True

                elif nums[mid]>val:
                    right=mid-1
                else:
                    left=mid+1

            return False
  
        for i in range(n-2):
            # x=self.binarysearch(nums[i+1:],nums[i]+diff)
            # y=self.binarysearch(nums[i+1:],nums[i]+(2*diff))
            currArray=nums[i+1:]
         
            x=binarysearch(currArray, nums[i]+diff)
            y=binarysearch(currArray,(nums[i]+(2*diff)))
            if x and y:
                cnt+=1

        return cnt