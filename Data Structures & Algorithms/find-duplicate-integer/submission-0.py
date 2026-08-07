class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #input: [1,2,3,2,2] -> look through the array and find repeat val -> output:repeat val
        nums.sort()
        for i in range(len(nums)):
            if(i>0 and nums[i-1]==nums[i]):
                return nums[i]

        

        