class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answers = set()
        for index, num in enumerate(nums):
            target = 0 - num
            seen = {}
            for index, j in enumerate(nums[(index+1):]):
                diff = target - j
                if diff in seen:
                    triplet = tuple(sorted([num, j, diff]))
                    answers.add(triplet)
                else:
                    seen[j] = index
        return [list(t) for t in answers]