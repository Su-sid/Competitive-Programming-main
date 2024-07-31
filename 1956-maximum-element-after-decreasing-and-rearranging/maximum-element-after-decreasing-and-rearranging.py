class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        # Step 1: Sort the array in ascending order
        arr.sort()

        # Initialize the maximum element after decrementing and rearranging
        max_element = 1

        # Step 2: Iterate through the sorted array
        for i in range(1, len(arr)):
            # Step 3: Ensure that the current element is at least one more than the previous maximum
            if arr[i] >= max_element + 1:
                max_element += 1

        # Step 4: Return the maximum element after the process
        return max_element