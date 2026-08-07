class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #[1,7,2,5,4,7,3,6]
        #l=1, r=7, water=36, mwater=36
        maxWater = 0
        l, r = 0, len(heights)-1
        while(l<r):
            water = min(heights[l],heights[r])*(r-l)
            maxWater = max(water,maxWater)
            if(heights[l]<heights[r]):
                l+=1
            elif(heights[l]>heights[r]):
                r-=1
            else:
                l+=1
                r-=1

        return maxWater