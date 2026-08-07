class MinStack:
    #["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]
    #arr=[], minValArr = [], len = 0
    def __init__(self):
        self.arr = []
        self.minValArr = []
        self.length = 0
        

    def push(self, val: int) -> None:
        self.arr.append(val)
        if(self.length==0):
            self.minValArr.append(val)
        else:
            self.minValArr.append(min(self.minValArr[self.length-1],val))
        self.length += 1


    def pop(self) -> None:
        self.arr.pop()
        self.minValArr.pop()
        self.length -= 1
        
    def top(self) -> int:
        return self.arr[-1]
        

    def getMin(self) -> int:
        return self.minValArr[-1]

        
