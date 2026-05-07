class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = [[] for _ in range(len(nums))]
        seen = defaultdict(int)

        for num in nums:
            seen[num] += 1
        
        for key, value in seen.items():
            count[value-1].append(key)
        
        res = []

        for j in range(len(count)-1, -1, -1):
            for num in count[j]:
                res.append(num)
                if len(res) == k:
                    break
            if len(res) == k:
                    break
        
        return res