class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) -1
        mVal = float("inf")
        while l<=r:
            mid = (l+r)//2
            mVal = min(nums[mid],mVal)
            print(mVal)
            if(nums[r]<nums[mid]):
                l = mid + 1
            else:
                r = mid -1
        
        return mVal
