class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #nums = [-1,0,2,4,6,8], target = 3
        #l =4, r= 6, m=5
        l,r = 0, len(nums)
        while(l<r):
            m = (l+r)//2
            if(nums[m]>target):
                r = m
            elif(nums[m]<target):
                l = m+1
            else:
                return m

        return -1