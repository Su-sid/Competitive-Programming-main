class Solution:
    def reverseWords(self, s: str) -> str:
        arr= (s.split()[::-1])
        # print(*arr)
        # Arr=  *arr
     
        return  " ".join(arr) 