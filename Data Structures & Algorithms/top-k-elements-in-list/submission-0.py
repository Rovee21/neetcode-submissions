class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myMap = {}

        for n in nums:
            myMap[n] = 1+myMap.get(n,0)
        
        sorted_dict = dict(sorted(myMap.items(), key=lambda item: item[1], reverse=True))

        result = []
        for i, key in enumerate(sorted_dict):
            if i>=k:
                break
            result.append(key)
        return result
        
        
