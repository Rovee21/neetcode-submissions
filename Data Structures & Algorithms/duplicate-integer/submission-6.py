class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #brute force: go through every combination and see if any match
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if(nums[i]==nums[j]):
        #             return True
        # return False

        #solution 2: create a hashmap and if the value is in the hashmap already return true
        # hm = {}
        # for i in range(len(nums)):
        #     if nums[i] in hm:
        #         return True
        #     hm[nums[i]] = i
        # return False

        #[1, 2, 3, 4]
        #set = 4, arr = 4
        #solution 3: set, compare the length of the set and array
        return len(set(nums))<len(nums)