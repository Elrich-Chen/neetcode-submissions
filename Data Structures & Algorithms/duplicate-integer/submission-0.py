class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = defaultdict(int)
        for num in nums:
            if seen[num] > 0:
                return True
            else:
                seen[num]+=1
        
        return False