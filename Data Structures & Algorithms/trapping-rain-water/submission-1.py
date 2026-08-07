class Solution:
    def trap(self, height: List[int]) -> int:

        if len(height) == 0:
            return 0
        
        lArr = []
        currL = 0
        for i in range(len(height)):
            currL = max(height[i],currL)
            lArr.append(currL)

        rArr = [0] * len(height)
        currR = 0
        i = len(height)-1
        while i>=0:
            currR = max(height[i],currR)
            rArr[i] = currR
            i -= 1
        
        #lArr = [0,2,2,3,3,3,3,3,3,3], 
        #rArr = [3,3,3,3,3,3,3,3,2,1], 
        #rainCount = 0
        #height = [0,2,0,3,1,0,1,3,2,1]

        rainCount = 0
        for j in range(len(height)):
            if(min(rArr[j],lArr[j])-height[j]>0):
                rainCount += min(rArr[j],lArr[j])-height[j]

        return rainCount
            


        