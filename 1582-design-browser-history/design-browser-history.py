class BrowserHistory:
    # use two stacks one for keeping the forward history and the primary one to keep backward history. 
    # Once you reach a back function cal, pop from backHistory stack and append popped value to forwardHistory stack. 
    # Once you reach a forward function cal, pop from forwardHistory stack and append popped value to backHistory stack. 

    def __init__(self, homepage: str):
        self.backHistory, self.forwardHistory= [], []
        self.visit(homepage)

    def visit(self, url: str) -> None:
        self.backHistory.append(url)
        self.forwardHistory= []

    def back(self, steps: int) -> str:
        # while len of backHistory stack is greater than 1 and steps is not == 0 pop from backHistory and append popped value to forwardHistory stack. 
      
        while len(self.backHistory) > 1 and steps:
            temp= self.backHistory.pop()

            self.forwardHistory.append(temp)
            steps-=1
           
        return self.backHistory[-1]
        

    def forward(self, steps: int) -> str:
    #    while stack is not empty and steps is not == 0 execute the while statement. 
        while self.forwardHistory and steps:
            temp= self.forwardHistory.pop()

            self.backHistory.append(temp)
            steps-=1

        # return the last/ top element of the backHistory stack
        return self.backHistory[-1]

        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forwardHistoryd(steps)