class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #input = [-1,0,1,2,-1,-4] ->find the values that add up to 0 in nums and put it in res arr->
        #output = [[-1,0,1], [-1,-1,2]] #edge case: len(nums) always greater than 3,
        #sort input = [-1,-1,0,1,2], output = [[-1,-1,2],[-1,0,1]]
        #i = 3, j = 4, k = 4

        nums.sort()
        res = set()
        for i in range(len(nums)-1):
            j = i+1
            k = len(nums) -1
            while(j<k):
                if(nums[i]+nums[j]+nums[k]==0):
                    res.add(tuple([nums[i],nums[j],nums[k]]))
                    j +=1
                    k -=1
                elif(nums[i]+nums[j]+nums[k]>0):
                    k -=1
                else:
                    j +=1

        resArr = []
        for i in res:
            resArr.append(i)
        
        return resArr


                
