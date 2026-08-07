class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #hashmap and return max elements
        countHM = {}
        for n in nums:
            countHM[n] = 1+countHM.get(n, 0)

        retArr = []
        for i in range(k):
            maxKey = max(countHM, key=countHM.get)
            retArr.append(maxKey)
            countHM.pop(maxKey)

        return retArr

