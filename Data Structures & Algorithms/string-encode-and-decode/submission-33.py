class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            delimiter = len(word)
            encoded += (str(delimiter) + "#" + word)
        return encoded

    def decode(self, s: str) -> List[str]:
        l, r = 0, 0
        decoded = []
        while l < len(s):
            j = l
            while s[j] != "#":
                j += 1
            length = int(s[l:j])
            res = s[j + 1 : j + 1 + length]
            decoded.append(res)
            l = j + 1 + length
        return decoded
