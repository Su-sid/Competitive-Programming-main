class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        
        n = len(nums)
        odd, even = [0] * n, [0] * n
        o, e = 0, 0

        # 1st iteration: get the odd sum and even sum
        for i, num in enumerate(nums):
            if i % 2:
                o += num
                odd[i] = o
                even[i] = e
            else:
                e += num
                even[i] = e
                odd[i] = o
        
        # 2nd iteration: check whether removing makes the array fair
        cnt = 0
        for i, num in enumerate(nums):
            cur_even, cur_odd = even[i], odd[i]
            post_even, post_odd = o - cur_odd, e - cur_even
            if i % 2:
                cur_odd -= num
            else:
                cur_even -= num
            
            if cur_even + post_even == cur_odd + post_odd:
                cnt += 1
        return cnt