class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        delim = "#"
        for s in strs:
            encoded += str(len(s)) + delim + s
        return encoded

    def decode(self, s: str) -> List[str]:
        res = []
        index = 0

        while index < len(s):
            r = index
            length = ""
            while s[r] != "#":
                length += s[r]
                r = r + 1
            
            length = int(length)
            word = s[r+1: r+1+length]
            res.append(word)

            index = r+length+1
        
        return res
