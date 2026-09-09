class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        shashmap = defaultdict(int)
        thashmap = defaultdict(int)
        for i in s:
            shashmap[i] += 1
        for j in t:
            thashmap[j] += 1

        return shashmap==thashmap

        


