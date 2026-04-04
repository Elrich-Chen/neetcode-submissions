class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights)-1
        largest = 0
        while l != r:
            area = min(heights[l],heights[r]) * (r-l)
            largest = max(largest,area)
            if (heights[l] <= heights[r]):
                l = l + 1
            else:
                r = r - 1
        return largest