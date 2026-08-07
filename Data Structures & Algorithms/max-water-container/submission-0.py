class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #[1,7,2,5,4,7,3,6]
        maxWater = 0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                water = min(heights[i],heights[j])*(j-i)
                maxWater = max(water,maxWater)

        return maxWater