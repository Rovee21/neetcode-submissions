class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #Input: intervals = [[0,2],[1,4],[3,5]]
        #Output: [[0,5]], prev[0,2]
        #[[0,2]]

        intervals.sort(key=lambda pair: pair[0])
        output = []
        prev = [0,-1]
        for i in range(len(intervals)):
            if(intervals[i][0]<=prev[1]):
                output.pop()
                output.append([min(prev[0],intervals[i][0]),max(intervals[i][1],prev[1])])
            
            else:
                output.append(intervals[i])
            prev = output[-1]
        
        return output