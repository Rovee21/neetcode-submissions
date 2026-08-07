class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #[1,2,4,6]
        #pre=[1,1,2,8], post=[48,24,6,1]

        #[1,1,2,8]
        preArr=[1]*len(nums)
        for i in range(len(nums)):
            if(i>0):
                preArr[i] = preArr[i-1]*nums[i-1]
       
        #[48,24,6,1]
        postArr=[1]*len(nums)
        for i in range(len(nums),-1,-1):
            if(i<len(nums)-1):
                postArr[i] = postArr[i+1]*nums[i+1]    
            
        retArr = []
        for i in range(len(preArr)):
            retArr.append(preArr[i]*postArr[i])

        return retArr

