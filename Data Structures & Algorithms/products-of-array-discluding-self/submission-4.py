class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #input:[1,2,4,6]
        #pre:[1,1,2,8]
        #post:[48,24,6,1]
        #return:[]

        pre = [1]*len(nums)
        post = [1]*len(nums)
        for i in range(1, len(nums)):
            pre[i] = nums[i-1]*pre[i-1]
        for j in range(len(nums)-2, -1, -1):
            post[j] = nums[j+1]*post[j+1]
        
        retArr = []
        for k in range(len(nums)):
            retArr.append(pre[k]*post[k])
        
        return retArr

