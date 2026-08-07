class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        tempCount = 0
        #[1, 5, 6,]
        #c=1, tc = 1
        for i in range(len(nums)):
            if(i!=0 and nums[i-1]==nums[i]):
                    continue
            elif(i==0 or i!=0 and nums[i-1]==(nums[i]-1)):
                tempCount+=1
                count =max(tempCount,count)
            else:
                tempCount = 1

        return count


