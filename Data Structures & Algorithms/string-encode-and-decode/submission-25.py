class Solution:

    def encode(self, strs: List[str]) -> str:
        password = ""
        key = "#"
        for string in strs:
            password = password + ((str(len(string)))+key+string)
        return password


    def decode(self, s: str) -> List[str]:
        i = 0 
        words = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j = j + 1
            length = s[i:j]
            i = j + 1 # start of the word now
            j = i + int(length)
            words.append(s[i:j])
            i = j #move index to starting of next word
        return words

        