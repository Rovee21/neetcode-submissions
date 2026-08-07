class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hset = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hset:
                return [hset[diff],i]
            hset[nums[i]] = i
        return []