# class Solution:
#     def countSubstrings(self, s: str) -> int: 
#         Acount= 0
#         def isPalindrome(word):
#             left, right= 0, len(word)-1
#             while left < right:  
#                 if word[left] != word[right]:
#                     return False 
#                 left += 1
#                 right -= 1
#             return True 
        

#         for i in range(len(s)):
#             for j in range(i, len(s)):
#                 if isPalindrome(s[i:j+1]):
#                     Acount+=1
#                     # print(s[i:j+1])

#         # print(Acount)
#         return Acount






class Solution:
    def countSubstrings(self, s: str) -> int:
        Acount = 0
        n = len(s)

        def expandAroundCenter(s, left, right):
            count = 0
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count

        # Loop through each possible center
        for center in range(n):
            # Odd length palindromes
            Acount += expandAroundCenter(s, center, center)
            # Even length palindromes
            Acount += expandAroundCenter(s, center, center + 1)

        return Acount
