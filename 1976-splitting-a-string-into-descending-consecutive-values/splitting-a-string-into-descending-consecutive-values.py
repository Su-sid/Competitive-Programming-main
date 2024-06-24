class Solution:
    def splitString(self, s: str) -> bool:
        length_of_s = len(s)

        def backtrack(i, val):
            if i == len(s): 
                return True

            for j in range(i,  len(s)):
                current = int(s[i:j + 1])
                if current + 1 == val:  # pruning 
                    if backtrack(j + 1, current):
                        return True
            
            return False

        # implement backtracking for every possible combinations. you will have length_of_s combinations for each tree branches
        # we will only loop until length_of_s - 1 because we need at least two elements to compare
        for i in range(length_of_s-1):
            if backtrack(i + 1, int(s[:i + 1])):
                return True

        return False