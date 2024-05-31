class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
            
        midpoint = 2 ** (n - 2)
       
        return self.kthGrammar(n - 1, k)  if k <= midpoint else 1 - self.kthGrammar(n - 1, k - midpoint)
       