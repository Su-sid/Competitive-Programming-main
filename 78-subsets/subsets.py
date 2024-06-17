class Solution:
    # def subsets(self, nums: List[int]) -> List[List[int]]:
        #create the recursive function
        # def create_subset(i):
        #     if i == len(nums):
        #         res.append(subset[:])
        #         return
            
        #     subset.append(nums[i])
        #     create_subset(i+1)

        #     subset.pop()
        #     create_subset(i+1)

        # res, subset= [], []
        # create_subset(0)
        # return res

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, path = [], []
        self.dfs(0, res, path, nums)
        return res
            
    def dfs(self, index, res, path, nums):
        res.append(list(path))     # 

        for i in range(index, len(nums)):

            path.append(nums[i])
            self.dfs(i+1, res, path, nums)
            print(path)
            # break
            path.pop()
    