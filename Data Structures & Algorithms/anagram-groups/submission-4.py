class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #["act","pots","tops","cat","stop","hat"]

        anaHM = defaultdict(list)

        for s in strs:
            sortS = "".join(sorted(s))
            anaHM[sortS].append(s)

        return list(anaHM.values())