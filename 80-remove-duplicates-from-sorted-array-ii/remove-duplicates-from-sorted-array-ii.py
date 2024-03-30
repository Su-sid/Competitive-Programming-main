class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
    
        slow = cnt_left = 0
        for num in nums:
            if slow == 0 or num != nums[slow - 1]: cnt_left = 2

            conditions = [
                num == nums[slow - 1] and cnt_left > 0,
                slow == 0,
                (num != nums[slow - 1])
            ]

            if any(conditions):
                nums[slow] = num
                slow += 1
                cnt_left -= 1

        return slow
            



                

            