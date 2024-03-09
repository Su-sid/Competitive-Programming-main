class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        k= k % n

        #flipping the first section
        left= 0
        right= n -k -1
        while left < right:  
                #   4           1              1            4
            nums[left], nums[right]= nums[right], nums[left]
            left +=1
            right-=1 
       
        
        #flipping the second section
        left= n -k
        right= n-1  
        while left < right:  
            nums[left], nums[right]= nums[right], nums[left]
            left +=1
            right-=1 
       
        
        #flipping the whole array
        # left= 0
        # right= n-1  
        # while left < right:  
              
        #     nums[left], nums[right]= nums[right], nums[left]
        #     left +=1
        #     right-=1 
        nums[:]= nums[::-1]
        


        # left= 1
        # right= len(nums)-1
        # i=0
        # nums=nums[::-1]
        # while left < right: #    
        #         nums[left], nums[right]= nums[right], nums[left]
        #         left +=1
        #         right-=1

        #     print(':',nums) #[7,1,2,3,4,5,6]
        #     i+=1
        #     #nums[::-1]

        # nums[:] = nums[-k:] + nums[:-k]
        

