class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        output= 0
        
        for i in range(len(operations)):
            
            if  operations[i] in ["++X", "X++"]:
                output+= 1
               
            elif operations[i] in ["--X", "X--"]:
                output-=1
               
            
         
            
        return  output      