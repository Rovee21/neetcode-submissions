class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)
        for s in strs:
            sortstr = "".join(sorted(s))
            hm[sortstr].append(s)
        
        retArr = []
        for sorStr in hm.values():
            retArr.append(sorStr)
        
        return retArr