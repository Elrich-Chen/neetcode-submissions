class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answers = []

        for i in range(len(nums)):
            ans = -(nums[i])
            seen = {}
            for j in range(i+1, len(nums)):
                if (i == j):
                    continue
                else:
                    res = ans - nums[j]
                    if res in seen:
                        temp = sorted([res, nums[j], nums[i]])
                        if temp not in answers: 
                            answers.append(temp)
                    else:
                        seen[nums[j]] = j 
        
        return answers