class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanString= ''.join(Achar.lower() for Achar in s if Achar.isalnum())
  
        left= 0 
        right= len(cleanString)
    
        while left < right:
            if cleanString[left] == cleanString[right-1]:
                right-=1
                left+=1
            else:
                return False
        return True



