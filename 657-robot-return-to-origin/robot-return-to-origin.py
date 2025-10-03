class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # // Solution 1:
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
        
        # // Solution 2:

        '''
        you can use a Counter object to check the count of moves for each direction you are stepping to 

        - For instance, given the directions U, D if the count is equal between the two pairs then it can be safely
        deduced that the robot moved to its destination and back to its original position
        '''

        from collections import Counter

        moves_count = Counter(moves)

        # print(moves_count)
        # Return the count for each direction pair 
        return (moves_count.get('U', 0) == moves_count.get('D', 0) and moves_count.get('L', 0) == moves_count.get('R', 0))

