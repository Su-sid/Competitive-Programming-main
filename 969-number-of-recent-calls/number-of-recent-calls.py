class RecentCounter:

    def __init__(self):
        #set an empty queue
        self.queue= deque()
        self.top=3000
        # self.final=null

    def ping(self, t: int) -> int:
        self.queue.append(t)

        while self.queue[-1]-self.top> self.queue[0]:
            self.queue.popleft()
        # print(self.queue) 
        return len(self.queue)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)