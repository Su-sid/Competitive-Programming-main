class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack= []
        
        final=[0]*len(temperatures)

        for i, temp in enumerate(temperatures):
            #use a stack as it accepts elements in a FIFO manner.
            while stack and temp> temperatures[stack[-1]]:
                # when current temp is > than the newest element in stack, pop the new element 
                # record the popped index and subtract the current index - popped index
                stackI = stack.pop()
                final[stackI]= i- stackI 
            stack.append(i)
         

        return final
        
        