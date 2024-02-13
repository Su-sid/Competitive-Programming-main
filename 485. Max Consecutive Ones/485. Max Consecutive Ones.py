class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        count= 0
        freq=[]

        for i in nums:
            #iterate over the whole array while identifying 1s in the array.
            # whenever you get not-1 you record the value of 1s found in "count" variable
            # after recording you need to continue the iteration till the end of len  of array.
          

            if i==1:
                #print('count1:',count)
                count+=1
           # If the current number is not 1 and count is not zero, append the count to freq
            else:
                if count > 0:
                    freq.append(count)
                count=0
        if count > 0:
            freq.append(count)
        count=max(freq,default=0)
        #print(sortArr)

        return(count)  
    


                    