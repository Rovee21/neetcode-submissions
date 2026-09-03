class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #optimal: hashset and go though the array and track if it is in hashset
        #i=0, hs={1}

        hashset = set()
        for i in range(len(nums)):
            if nums[i] in hashset:
                return True
            hashset.add(nums[i])
        
        return False
        