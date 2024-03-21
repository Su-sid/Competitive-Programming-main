class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        top= counter= lastindex= bottom= 0 
        final=[]
        length= len(s)  
        while bottom < length:
            #get the last index of the character on the first pointer. 
            lastindex= s.rindex(s[bottom])
            top = max(lastindex, top)
            counter+=1
            if top==bottom:
                final.append(counter)
                bottom+=1
                top+=1
                counter=0
            else:
                bottom+=1
        return final
