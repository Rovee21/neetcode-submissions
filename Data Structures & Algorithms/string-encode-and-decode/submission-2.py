class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s))+ " " + s
        return result

    def decode(self, s: str) -> List[str]:
        arr = []
        i = 0
        while i<len(s):
            j = i
            while s[j]!=" ":
                j +=1
            length = int(s[i:j])
            i=j+1
            j = i + length
            arr.append(s[i:j])
            i = j

        return arr;

