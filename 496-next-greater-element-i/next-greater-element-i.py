class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap= {}

        #fill the hashmap with key:-1
        for num in nums1:
            hashmap[num]=-1
        store = []


        #iterate checking the next greater element and replacing in the hashmap
        for num in nums2:
            while store and num > store[-1]:
                top = store.pop()
                if top in hashmap: 
                    
                    hashmap[top] = num
            store.append(num)
        final= hashmap.values()
        return final