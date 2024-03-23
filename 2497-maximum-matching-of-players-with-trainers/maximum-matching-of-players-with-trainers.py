class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        count=0       
        slow, fast=0,0 
        while slow < len(players) and fast < len(trainers):
            if players[slow]<= trainers[fast]:
                fast +=1
                slow +=1
                count +=1
            else:
                fast+=1
        return count
        