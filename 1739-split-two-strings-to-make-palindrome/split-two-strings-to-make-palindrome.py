class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        self.n = len(a)
        f = 0
        s = 0
        l = 0 
        r = self.n -1 
        while l < r and a[l]==b[r]:
            l+=1
            r-=1
        if l>r or a[l:r+1]==a[l:r+1][::-1] or b[l:r+1]==b[l:r+1][::-1]:
            return True

        a,b = b,a
        l = 0 
        r = self.n -1 
        while l < r and a[l]==b[r]:
            l+=1
            r-=1
        if l>r or a[l:r+1]==a[l:r+1][::-1] or b[l:r+1]==b[l:r+1][::-1]:
            return True
        
       
        