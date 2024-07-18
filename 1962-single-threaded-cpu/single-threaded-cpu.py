class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]: 
        for i, task in enumerate(tasks):
            task.append(i)
        tasks.sort(key=lambda task: task[0])
        # print(tasks)
        heap=[]
        final=[]

        task, time = 0, tasks[0][0]#set time to the first enque time

        # while heap has values or list is not at end
        while heap or task <len(tasks):
            #add task(s) which enque time is less than the current time only. 
            while task <len(tasks) and time >= tasks[task][0]:
                heapq.heappush(heap, (tasks[task][1], tasks[task][2]))
                task+=1
            
            # if the heap is not empty, add time of task and update final list
            if heap:
                processingTime, index= heapq.heappop(heap)
                final.append(index)
                time +=processingTime
            #if heap is empty add the enque time of the given task
            else:
                time= tasks[task][0]
            # return the final list
        return final




        




        # final= list()
        # heap=[]
        # time=1
        # for i, task in enumerate(tasks):
        #     if heap:
        #         heappush(heap, (task[1],  task[2]) # task[1]==time to process task[2]==index of  task  
        #     else:
        #         time+= task[1]

        # # for i, task in enumerate(tasks):
        # print(tasks)






