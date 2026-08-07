class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #integer vals

        #easy solution: time: O(n^2) space=O(1), going through every index and seeing if there is a match

        #optimal solution: time: O(n) space=O(n), going through each element and adding it to the hashmap
        #subtracting the target by the value that the index is on and seeing if it is in the hashmap

        hm = {}
        for i in range(len(nums)):
            val = target-nums[i]
            if val in hm:
                return [hm.get(val),i]
            hm[nums[i]] = i
