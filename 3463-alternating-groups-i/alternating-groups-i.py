class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        Acount=0
        n =len(colors)

        for i in range(n):
            if colors[i%n]== colors[(i+2)%n] and colors[i%n] !=colors[(i+1) %n]:
                Acount+=1
        return Acount



        