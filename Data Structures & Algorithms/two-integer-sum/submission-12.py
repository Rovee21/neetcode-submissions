class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #brute force: loop through and find every combination in the array
        for i in range(len(nums)):
            j = i+1
            while(j<len(nums)):
                if(nums[i]+nums[j]==target):
                    return [i,j]
                j += 1
            
        #hashmap and go through nums if target
        visited = {}
        for i in range(len(nums)):
            if(target-nums[i] in visited):
                return [visited[target-nums[i]],i]
            visited[nums[i]] = i
        