class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #words = {}
        #loop strs
            #have an empty a->z cahracter 27 length array
            #fill up our counts
            #use this as the key to our dictinary and append it to the list
        #output each item in the dict
        words = {}
        for string in strs:
            count = [0 for i in range(27)]
            for letter in string:
                count[ord(letter) - ord('a')] += 1
            key = tuple(count)

            if key in words:
                words[key].append(string)
            else:
                words[key] = [string]
        
        res = []

        for key,value in words.items():
            res.append(value)
        return res
