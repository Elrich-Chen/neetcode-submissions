class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = defaultdict(list)
        res = []
        
        for string in strs:
            count = [0] * 26

            for char in string:
                count[ord(char) - ord('a')] += 1
            
            words[tuple(count)].append(string)
        
        for key, value in words.items():
            res.append(value)
        
        return res
    
