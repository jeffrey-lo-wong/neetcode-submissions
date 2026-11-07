class Solution:
    def trap(self, height: List[int]) -> int:
        # looking for the most amount of water trapped
        # the conditions for water to be trapped
        # the opening must be surrounded by two pillars
        # limited by the smaller pillar

        if not height:
            return 0 
            
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res

             
