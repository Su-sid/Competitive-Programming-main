class Solution:
    def hIndex(self, citations: List[int]) -> int:

        
        # left= 0
        # right= n

        def binarySearch( array):
            left=0
            length= len(array)
            right=length -1
            ans=0

            while left<= right:
                mid= left+(right-left)//2
                papers= length -mid

                if papers <= array[mid]:

                   ans=papers

                   right= mid-1
                else:
                    left = mid + 1
            return ans

        return binarySearch(citations)

        