class MinStack:

    def __init__(self):
        self.values = list()
        
    def push(self, val: int) -> None:
        self.values.append(val)

    def pop(self) -> None:
        self.values = self.values[:-1]

    def top(self) -> int:
        top_val = self.values[-1:][0]
        return top_val

    def getMin(self) -> int:
        return min(self.values)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()