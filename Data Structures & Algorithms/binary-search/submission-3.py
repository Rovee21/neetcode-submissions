class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #[5], target 5
        #l= 0, r = 0, m =
        l=0
        r=len(nums)
        while(l<r):
            m = (l+r)//2
            if(nums[m]>target):
                r = m
            elif(nums[m]<target):
                l = m+1
            else:
                return m

        return -1
