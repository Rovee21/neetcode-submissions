class Solution:
    def findMin(self, nums: List[int]) -> int:
        #input:[3,4,5,6,1,2] -> find the minimum element ->return: 1
        #edge cases: len(nums)>0
        #easy thing to do go through every element and track min
        #optimal: l, r, m, input= [3,4,5,1,2], output was 3
        #result=3, l=3, r=4, m=3

        res = nums[0]
        l = 0
        r = len(nums)-1
        while l<=r:
            if(nums[l]<nums[r]):
                res = min(res,nums[l])
                break
            
            m = (l+r)//2
            res = min(res,nums[m])
            if(nums[m]>=nums[l]):
                l = m+1
            else:
                r = m-1

        return res
