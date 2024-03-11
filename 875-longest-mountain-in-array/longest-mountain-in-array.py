class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        left,right,ans = 0,0,0
        for i in range(1, len(arr)):
            if (right and arr[i-1] < arr[i]) or arr[i-1] == arr[i]:
                left,right = 0, 0
            left += arr[i-1] < arr[i]
            right += arr[i-1] > arr[i]

            if left  and right:
                ans = max(ans, left + right + 1)
        return ans    