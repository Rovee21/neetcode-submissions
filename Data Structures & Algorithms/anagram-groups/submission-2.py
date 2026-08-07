class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myMap = {}
        for s in strs:
            word = "".join(sorted(s))
            if word not in myMap:
                myMap[word] = []
            myMap[word].append(s)

        return list(myMap.values())
        
