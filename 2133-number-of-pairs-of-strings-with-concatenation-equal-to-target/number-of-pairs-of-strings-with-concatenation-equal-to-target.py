class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        # Step 1: Count occurrences of each string in nums
        d = {} 
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        count = 0
        # Step 2: Iterate over each key in the dictionary
        for key, value in d.items():
            # Check if the key can be a prefix of the target
            if target.startswith(key):
                # Find the corresponding suffix needed to complete the target
                suffix = target[len(key):]
                # Check if the suffix exists in the dictionary
                if suffix in d:
                    if suffix == key:
                        # If the prefix and suffix are the same string, use combinatorial counting
                        count += value * (value - 1)
                    else:
                        # Count pairs between different strings
                        count += value * d[suffix]

            

        return count