class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #[48,24,12,8]
        #prefix=[1,1,2,8],postfix=[48,24,6,1]

        prefixArr = []
        prefixVal = 1
        for n in nums:
            prefixArr.append(prefixVal)
            prefixVal *= n
        
        postfixArr = [1] * len(nums)
        postfixVal = 1
        i = len(nums) -1
        while i>=0:
            postfixArr[i] = postfixVal
            postfixVal *= nums[i]
            i-=1
        
        for j in range(len(nums)):
            nums[j] = postfixArr[j]*prefixArr[j]
        
        return nums


        

