class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #brute force solution is to iterate through each index and look for every possible combination, time: O(n^2)
        #[4,5,6]
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if(nums[i]+nums[j]==target):
                    return [i,j]




