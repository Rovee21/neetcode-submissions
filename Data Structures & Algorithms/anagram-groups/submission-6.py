class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                pos = ord(c)-ord("a")
                count[pos] += 1
            hm[tuple(count)].append(s)
        
        retArr = []
        for sorStr in hm.values():
            retArr.append(sorStr)
        
        return retArr