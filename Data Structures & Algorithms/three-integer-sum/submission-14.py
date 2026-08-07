class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #brute force: go through pairing to try to find solutions
        #[-1,0,1,2,-1,-4]
        #[-4,-1,-1,0,1,2]
        #[[-1,-1,2],[-1,0,1]]

        nums.sort()
        retArr = []
        for i in range(len(nums)):
            if(i>0 and nums[i-1]==nums[i]):
                continue
            j = i+1
            k = len(nums)-1
            while(j<k):
                if(nums[i]+nums[j]+nums[k]==0):
                    retArr.append([nums[i],nums[j],nums[k]])
                    j+=1
                    while(j<k and nums[j-1]==nums[j]):
                        j+=1
                    k-=1
                elif(nums[i]+nums[j]+nums[k]>0):
                    k-=1
                else:
                    j+=1

        return retArr




        