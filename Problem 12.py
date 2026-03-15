# Container With Most Water

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            # Current width between two pointers
            width = right - left

            # The height of the water is determined by the shorter line
            current_height = min(height[left], height[right])

            # Update the maximum area found so far
            max_area = max(max_area, current_height * width)

            # Strategy : Move the pointer that points to the shorter line
            if height[left] < height[right]:
                left = left + 1
            else:
                right = right - 1

        return max_area

        
