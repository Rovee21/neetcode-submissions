class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #brute force solution is to iterate through each index and look for every possible combination, time: O(n^2)
        #[4,5,6]
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if(nums[i]+nums[j]==target):
        #             return [i,j]

        """
        hashmap, go through every indecies, if the target minus
        the value is not in the hashmap, then we can add that value to the hashmap
        and keep going till the target is found"""
        
        #4,5,6, target = 10
        hm = {}
        for i in range(len(nums)):
            goalVal = target-nums[i]
            if goalVal in hm:
                return [hm.get(goalVal), i]
            hm[nums[i]] = i


        
        





