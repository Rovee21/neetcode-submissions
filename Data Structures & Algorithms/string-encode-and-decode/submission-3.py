class Solution:

    #[hi, there]
    def encode(self, strs: List[str]) -> str:
        retStr = ""
        for s in strs:
            retStr += str(len(s)) + "#" + s
        
        return retStr
            

    def decode(self, s: str) -> List[str]:
        retArr = []
        i = 0
        while i<len(s):
            count = ""
            while s[i]!="#" and i<len(s):
                count += s[i]
                i += 1
            i+=1
            count = int(count)
            retArr.append(s[i:(i+count)])
            i += count
        
        return retArr





            

