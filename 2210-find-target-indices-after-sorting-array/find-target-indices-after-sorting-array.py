class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums = sorted(nums)
        print(nums)
        index_of_nums=defaultdict()
        index_list=list()

        for i , num in enumerate(nums):

            if num in index_of_nums:
                index_of_nums[num].append(i)
            else:
                index_of_nums[num]=[i]

        return index_of_nums.get(target,[])
        