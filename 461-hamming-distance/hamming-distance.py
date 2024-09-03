class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        
        # # Calculate the number of set bits in the XOR
        # distance = 0
        # while xor:
        #     xor &= xor - 1
        #     distance += 1
        
        # return distance
        return bin(xor).count('1')