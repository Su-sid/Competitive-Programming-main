class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr_dict= defaultdict(list)

        print(arr_dict)

        for i, num in enumerate(nums):
            arr_dict[num].append(i)
        
        sort_arr= sorted(nums)
        left= 0
        right= len(sort_arr)-1
        print(arr_dict)
       
        while left < right:
            if sort_arr[left] + sort_arr[right] == target:
                return [arr_dict[sort_arr[left]][0], arr_dict[sort_arr[right]][-1] ]

            elif sort_arr[left] + sort_arr[right] < target:
                left +=1
            else:
                right-=1



                

        