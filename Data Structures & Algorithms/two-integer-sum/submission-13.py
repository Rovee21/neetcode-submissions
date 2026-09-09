class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i in range(len(nums)):
            tval=target-nums[i]
            if tval in hm:
                return [hm[tval], i]
            hm[nums[i]] = i
        
