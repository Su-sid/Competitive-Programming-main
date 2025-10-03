class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # x, y = 0, 0

        # for i in moves:
        #     if i == "U":
        #         y +=1
        #     if i == "D":
        #         y -=1
        #     if i == "R":
        #         x +=1
        #     if i == "L":
        #         x -=1
        
        # return ( x == 0 and y == 0)

        '''
        you can also use a Counter to check the number of moves of each direction you are stepping to 

        - For instance, given the directions U, D if the count is equal between the two pairs then it can be safely
        deduced that the robot moved back to its original position
        '''

        from collections import Counter

        moves_count = Counter(moves)

        print(moves_count)

        return (moves_count.get('U', 0) == moves_count.get('D', 0) and moves_count.get('L', 0) == moves_count.get('R', 0))

