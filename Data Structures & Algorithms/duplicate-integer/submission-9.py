class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #brute force
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if(nums[i]==nums[j]):
        #             return True

        # return False

        #optimal solution: use set and see if item is in set
        dupChecker = set()
        for n in nums:
            if n in dupChecker:
                return True
            dupChecker.add(n)
        
        return False
