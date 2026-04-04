class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        arr = [[] for i in range(len(nums)+1)]

        for key,value in count.items():
            arr[value].append(key)
        
        result = []

        for i in range(len(arr)-1, 0, -1):
            for n in arr[i]:
                result.append(n)

        return result[:k]

        