class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        shifts= 0    
        # def isSorted(nums ):
        #     return all(nums [i] <= nums [i+1] for i in range(len(nums ) - 1))
        # # print(isSorted(nums))

        def sorterFunction(nums, shifts):
            n = len(nums)
            
            largest = nums[-1]

            for i in range(n-2, -1, -1): 
                #start from the  second last index backwards
                # check if its bigger than the largest index
                if nums[i] <= largest:
                    largest= nums[i]
                    continue 
                else:
                    # if bigger break it down into two that  smaller is larger than
                    # previuos value
                    divideBy=(nums[i] + largest - 1) // largest 

                    shifts+= divideBy-1

                    largest =nums[i] // divideBy
            return shifts
        
        # if  isSorted(nums):
        #     return shifts
        # else:
        return sorterFunction(nums, shifts)
