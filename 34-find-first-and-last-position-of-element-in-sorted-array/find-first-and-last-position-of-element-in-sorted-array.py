class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findFirst(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    if mid == 0 or nums[mid - 1] != target:
                        return mid
                    else:
                        right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
        
        def findLast(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    if mid == len(nums) - 1 or nums[mid + 1] != target:
                        return mid
                    else:
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
        
        first = findFirst(nums, target)
        last = findLast(nums, target)
        return [first, last]



# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         left, right= 0, len(nums)-1

#         final=[]
#         # length = len(nums)-1

#         while left <= right :
#             mid = left+ (right-left) // 2

#             if nums[mid]== target:
#                 final.append(mid)
#             elif nums[mid] < target:
#                 left= mid+1
#             elif nums[mid] > target:
#                 right= mid-1

#             # else:
#             #     return [-1,-1]
# # Binary Search : 

# # we use simply Binary Search algorithms , and in return statement (when our conditon get True that is ( nums[mid] == target )) before returing we check for lower index ( that is "index" less than mid ) if their is "lower index" which is less than "mid" index then we return that "index" , and if their is not such "index" means (l_index == -1) so we return "mid" , similarly for right side (ending position ), and we also use "left_bool" which help us in finding starting or ending position (if left_bool = True means we are finding starting position and if left_bool = False means ending position )
# ##

#         return final 

