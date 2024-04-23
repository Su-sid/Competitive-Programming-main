class DataStream:

    def __init__(self, value: int, k: int):
        self.val = value
        self.k = k
        self.queue =deque()
        self.stream = collections.defaultdict(int)

    def consec(self, num: int) -> bool:
        self.queue.append(num)
        self.stream[num] += 1
        if len(self.queue) > self.k:
            rmv = self.queue.popleft()
            self.stream[rmv] -= 1
        return self.stream[self.val] == self.k
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
