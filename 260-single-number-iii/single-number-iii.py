class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        Acount= Counter(nums) 
        final= list()  

        # print(Acount)      
        for i in Acount:
            # print(Acount[i])
            if Acount[i]== 1:
                final.append(i)

        return final
