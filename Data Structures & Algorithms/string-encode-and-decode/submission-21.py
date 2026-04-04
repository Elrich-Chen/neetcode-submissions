class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs:
            password = ""
            key = "#"
            for string in strs:
                password = password + ((str(len(string)))+key+string)
            return password
        return ""


    def decode(self, s: str) -> List[str]:
        if s:
            words = []
            index = 0
            key = "#"
            while index < len(s):
                number = ""
                while s[index] != key:
                    number += s[index]
                    index = index + 1
                word = ""
                number = int(number)
                for i in range(number):
                    index = index + 1
                    word += s[index]
                words.append(word)
                index = index + 1
            return words
        return []
        