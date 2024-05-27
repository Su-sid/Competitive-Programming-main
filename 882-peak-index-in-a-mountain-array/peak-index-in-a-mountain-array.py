class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:


        left=0
        right=len(arr)-1


        while left < right:

            mid =  left + (right - left) // 2
            if arr[mid-1]<=arr[mid] and arr[mid+1]<=arr[mid]:
                return mid
            elif arr[mid-1]>arr[mid]:
                right=mid
            else:
                left=mid  
   




        

