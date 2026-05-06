class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word = [0] * 27

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            word[ord(s[i]) - ord("a")] += 1
            word[ord(t[i]) - ord("a")] -= 1
        
        for i in word:
            if i != 0:
                return False
        
        return True
        