class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answers = []
        for index in range(len(nums)):
            if index > 0 and nums[index] == nums[index - 1]:
                continue

            target = -(nums[index])
            l, r = index+1, len(nums)-1

            while (l < r):
                res = nums[l] + nums[r]
                if res > target:
                    r = r - 1
                elif res < target:
                    l = l + 1
                else:
                    answers.append([nums[index], nums[l], nums[r]])
                    l = l + 1
                    while l < r and nums[l] == nums[l - 1]:
                        l = l + 1

        return answers
            
             