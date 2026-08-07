class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_hashset = set()
        for i in nums:
            if i in my_hashset:
                return True
            my_hashset.add(i)

        return False