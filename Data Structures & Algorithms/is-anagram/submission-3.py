class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word1 = [0] * 27
        word2 = [0] * 27

        for i in s:
            word1[ord(i) - ord("a")] += 1

        for i in t:
            word2[ord(i) - ord("a")] += 1
        
        for i in range(26):
            if word1[i] == word2[i]:
                continue
            else:
                return False
        
        return True
        