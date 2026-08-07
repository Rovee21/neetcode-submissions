class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #nums = [0,3,2,5,4,6,1,1]
        #set={0,1,2,3,4,5,6}
        numSet = set(nums)
        longest = 0
        #longest = 0, tempC = 2, nVal = 2
        for n in nums:
            if n-1 not in numSet:
                tempCount = 1
                nVal = n+1
                while nVal in numSet:
                    tempCount += 1
                    nVal += 1
                longest = max(longest,tempCount)
        
        return longest


