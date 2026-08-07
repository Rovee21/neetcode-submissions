class Solution:
    def findMin(self, nums: List[int]) -> int:
        #input:[3,4,5,6,1,2] -> find the minimum element ->return: 1
        #edge cases: len(nums)>0
        #easy thing to do go through every element and track min

        res = 1001
        for n in nums:
            res = min(res,n)
        return res