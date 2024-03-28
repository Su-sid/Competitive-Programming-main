class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        length= fast= slow= 0
        store = defaultdict(int)

        
        for fast in range(len(fruits)):
            store[fruits[fast]] +=1

            while len(store)==3:
               store[fruits[slow]]  -= 1

               if store[fruits[slow]]==0:
                  del store[fruits[slow]]
                
               slow+=1

            length= max(length, fast+1-slow)


        return length 
                  

            # fruit

        