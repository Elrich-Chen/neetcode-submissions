class Solution:
    def trap(self, height: List[int]) -> int:
        amt = 0
        if not height:
            return amt
        
        l,r = 0, len(height)-1
        leftMax = height[l]
        rightMax = height[r]
        while l < r:
            if leftMax < rightMax:
                l = l + 1
                leftMax = max(leftMax, height[l])
                amt += leftMax - height[l]
            else:
                r = r - 1
                rightMax = max(rightMax, height[r])
                amt += rightMax - height[r]
        return amt
                

        