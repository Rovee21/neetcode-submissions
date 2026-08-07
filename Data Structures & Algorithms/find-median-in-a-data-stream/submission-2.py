class MedianFinder:

    def __init__(self):
        self.arr = []
        self.numElements = 0

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.numElements+=1
        

    def findMedian(self) -> float:
        self.arr.sort()
        if self.numElements%2==1:
            return (float)(self.arr[(self.numElements//2)])
        else:
            return (float)((self.arr[(self.numElements//2)]+self.arr[(self.numElements//2)-1])/2)

        
        