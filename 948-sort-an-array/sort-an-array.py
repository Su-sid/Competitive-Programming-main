class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        '''
        For mergeSort you have to:
        1. develop the sort function that will recursively call itself to split the main array into chunks. Also define the middle INDEX of the main array. 
        2. develop the merge function that compares the first elements of the developed subarrays. 
        3. if the first element of the leftArray is <= rightArray, then add the least element to the final array and vice versa. 
        4.
        '''
        def merge (leftArr,rightArr ):
            # pass
            finalArr= []
            left, right = 0, 0
            # traverse all the elements in the array and if some remain traverse them too. 
            while left < len(leftArr) and right < len(rightArr):

                if leftArr[left] <= rightArr[right]:
                    finalArr.append(leftArr[left])
                    left+=1
                else:
                    finalArr.append(rightArr[right]) 
                    right+=1

            while left < len(leftArr):
                finalArr.append(leftArr[left])
                left+=1
            while right < len(rightArr):
                finalArr.append(rightArr[right])
                right+=1
            return finalArr

        def mergeSort(array):
                   
            if len(array) <2:
                return array

            mid = len(array) //2
            # divide and conquer approach
            leftArr= mergeSort(array[:mid])
            rightArr= mergeSort(array[mid:])
            # print(leftArr)
            # print(rightArr)
            return merge(leftArr, rightArr)

        return mergeSort(nums)
