class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:  
        solutions =list()
        state= list()
        self.search(state,solutions, n)
        return solutions

    def is_valid_state(self, state, n):
        # check if a state is a valid solution
        return  len(state)== n 

    def get_candidates(self, state, n):
        if not state:
            return range(n)
        #find the next position to populate

        position= len(state)
        candidates= set(range(n))

        for row, col in enumerate(state):
        # discard a column index if its occupied
            candidates.discard(col)
            distance= position -row
            candidates.discard(col+distance)
            candidates.discard(col-distance)
        return candidates

    def search(self, state, solutions, n ):
        if self.is_valid_state( state, n):

            state_string= self.index_to_string( state, n )

            solutions.append(state_string)
            return
        
        for candidate in self.get_candidates(state,n ):
            state.append(candidate)
            self.search(state, solutions, n)
            state.pop()
    
    def index_to_string(self, state, n ):
        res= []
        for i in state:
            string= '.'*i +'Q'+'.'*(n-i-1)
            res.append(string)
        return res