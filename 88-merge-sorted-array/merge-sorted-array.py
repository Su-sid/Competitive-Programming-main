class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        total= m+n 
        l=0
        r=0
        #replace 0's with values from nums2
        while l< total:
            if nums1[l]==0 and r< n:
                nums1[l]=nums2[r]
                r+=1
            l+=1
        # two pointer sorting technique
        slow=0
        while slow<total-1:
            fast= slow+1
            while fast< total:
                if nums1[slow]>nums1[fast]:
                    nums1[slow],nums1[fast]=nums1[fast],nums1[slow]
                fast+=1
            slow+=1
    