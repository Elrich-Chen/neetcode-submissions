class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #i would have tried to do in O(n) using division operation
        #prefix array - all products on left side
            # [1, ... ]
        #postfix array - all products on the right side
            # [..., 1]
        
        prefix = [1] * (len(nums))
        for index in range(1, len(nums)):
            prefix[index] = nums[index-1] * prefix[index-1]

        postfix = [1]*len(nums)
        for index in range(len(nums)-2, -1, -1):
            postfix[index] = nums[index+1] * postfix[index+1]
        
        result = []
        for index in range(len(nums)):
            result.append(prefix[index]*postfix[index])
        return result