class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
       # return set(nums1)& set(nums2)

        output = []
        sorted_arr_1 = sorted(nums1)
        sorted_arr_2 = sorted(nums2)

        left = 0
        right = 0

        while left < len(sorted_arr_1) and right < len(sorted_arr_2):
            if sorted_arr_1[left] < sorted_arr_2[right]:
                left += 1
            elif sorted_arr_2[right] < sorted_arr_1[left]:
                right += 1
            else:
                output.append(sorted_arr_1[left])
                left += 1
                right += 1
        return output