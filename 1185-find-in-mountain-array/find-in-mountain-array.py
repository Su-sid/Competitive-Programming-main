class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        #find peak
        def find_peak(length, mountain_arr):
            left = 1
            right = length - 2
            while left <= right:
                mid = left + (right-left)//2
                left_value = mountain_arr.get(mid - 1)
                mid_value = mountain_arr.get(mid)
                right_value = mountain_arr.get(mid + 1)
                if left_value < mid_value < right_value:
                    left  = mid + 1
                elif left_value > mid_value > right_value:
                    right = mid - 1
                else:
                    return mid
        
        #search left
        def search_left(peak,mountain_arr):
            left = 0
            right = peak

            while left <= right:
                mid = left + (right-left)//2
                mid_value = mountain_arr.get(mid)

                if mid_value < target:
                    left = mid + 1
                elif mid_value > target:
                    right = mid - 1
                else:
                    return mid
            return -1
        
        #search right
        def search_right(peak,length,mountain_arr):
            left = peak
            right = length - 1

            while left <= right:
                mid = left + (right-left)//2
                mid_value = mountain_arr.get(mid)
                if mid_value > target:
                    left = mid + 1
                elif mid_value < target:
                    right = mid - 1
                else:
                    return mid
            return -1
        ans=-1
        length = mountain_arr.length()
        peak = find_peak(length,mountain_arr)
        ans = search_left(peak,mountain_arr)

        if ans == -1:
            ans = search_right(peak,length,mountain_arr)
    
        return ans