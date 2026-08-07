class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #get each number make it a key in the hashmap and the value would be how many times it appeared
        #[1,2,2,3,3,3]
        hm = {}
        for num in nums:
            hm[num] = 1 + hm.get(num, 0)
        
        #{1:1}. k=2
        returnArr = []
        for i in range(k):
            maxVal = max(hm, key= hm.get)
            returnArr.append(maxVal)
            hm.pop(maxVal)
        
        #[3, 2]
        return returnArr

        