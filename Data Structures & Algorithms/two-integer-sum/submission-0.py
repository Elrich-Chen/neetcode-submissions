class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        
        for index, number in enumerate(nums):
            diff = target - number
            if diff not in seen:
                seen[number] = index
            else:
                return [seen[diff], index]