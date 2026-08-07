class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #take the value a and try to find the two sum with the remaining values
        #sort the array first
        #-1,0,1,2,-1,-4
        #sortArr = [-4,-1,-1,0,1,2]
        #n=-1 l=-1, r=2, resArr = []
        sortArr = sorted(nums)
        resArr = []
        for i in range(len(sortArr)):
            if sortArr[i]>0:
                break
            if(i>0 and sortArr[i]==sortArr[i-1]):
                continue
            l = i+1
            r = len(sortArr)-1
            while(l<r):
                threeSum = sortArr[i] + sortArr[l] + sortArr[r]
                if(threeSum<0):
                    l+=1
                elif(threeSum>0):
                    r-=1
                else:
                    resArr.append([sortArr[i],sortArr[l],sortArr[r]])
                    l+=1
                    r-=1
                    while(l<r and sortArr[l]==sortArr[l-1]):
                        l+=1
        
        return resArr
