class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        word1 = {}
        for c in s:
            word1[c] = word1.get(c, 0) + 1

        word2 = {}
        for c in t:
            word2[c] = word2.get(c, 0) + 1
        
        return word1 == word2