class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largest = 0
        area = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            if heights[l] > heights[r]:
                area = heights[r] * (r - l)

                if area > largest:
                    largest = area

                r = r - 1

            else: 
                area = heights[l] * (r - l)

                if area > largest:
                    largest = area
                    
                l = l + 1

        return largest                 


            
