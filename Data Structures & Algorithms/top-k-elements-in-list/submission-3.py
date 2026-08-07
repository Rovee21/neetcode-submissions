class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #[1,2,3,4,5,6] k=6
        
        #{1:1, 2:2, 3:3}
        countHm = {}
        for n in nums:
            countHm[n] = 1+countHm.get(n, 0)
        #[[],[1,2,3,4,5,6],[],[],[],[],[]]
        countArr = [[] for i in range(len(nums)+1)]
        for i, c in countHm.items():
            countArr[c].append(i)
        #go backwards until res arr is len of k
        retArr = []
        for i in range(len(countArr)-1,0,-1):
            for n in countArr[i]:
                retArr.append(n)
                if(len(retArr)==k):
                    return retArr

                