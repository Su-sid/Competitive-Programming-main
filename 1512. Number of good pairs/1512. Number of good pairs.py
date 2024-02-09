class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        good_pairs = 0

        #a dictionary to track counts of each element
        element_counts = {}

        # Iterate through the array
        for element in nums:
            # Check if the element has been encountered before
            if element in element_counts:
                # calculate and add the good pairs for this element
                good_pairs += element_counts[element] 
            element_counts[element] = element_counts.get(element, 0) + 1 

        return good_pairs
