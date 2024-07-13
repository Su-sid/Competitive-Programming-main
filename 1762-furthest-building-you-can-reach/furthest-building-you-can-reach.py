class Solution:

    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        maxheap=[]
        prev=heights[0]
    
        for i in range(len(heights)-1):
            nextheight,height =heights[i+1],  heights[i] 

            difference = nextheight - height
            if difference <=0:
                continue
            heappush(maxheap, -difference)
            # print(maxheap)
            bricks-= difference
            
            if bricks < 0:
                if ladders ==0:
                   return i
                #add back the bricks and reduce the ladders 
                bricks+= -(heappop(maxheap))
                # print('::',bricks)
                ladders-=1
     
        return len(heights)-1


            
            