class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        moves=0
        while target > 1:
            
            if maxDoubles and target%2==0: 
                #if maxDoubles is not 0 and target always is divided by 2 & add 1 to moves 
                maxDoubles-=1
                target//=2
                moves+=1
            else:
                # decrement target by 1 and increment moves by 1
                target-=1
                if not maxDoubles:
                    return target+moves

                moves+=1
        return moves


