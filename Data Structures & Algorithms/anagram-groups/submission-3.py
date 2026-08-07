class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #sorting w hashmap: {sorted word: [original word]
        sortHM = defaultdict(list)
        for i in range(len(strs)):
            sortStr = "".join(sorted(strs[i]))
            sortHM[sortStr].append(strs[i])
        
        arr = []
        for key in sortHM:
            arr.append(sortHM.get(key))
        
        return arr