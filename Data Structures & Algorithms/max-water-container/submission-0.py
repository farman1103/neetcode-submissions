class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = -1
        left = 0
        right = len(heights) -1
        while left < right :
            length = right - left
            if heights[left] - heights[right] > 0:
                height = heights[right]
                area = length * height
                right -= 1
            elif heights[left] - heights[right] < 0:
                height = heights[left]
                area = length * height
                left += 1
            elif heights[left] - heights[right] == 0:
                height = heights[right]
                area = length * height
                right -=1
                left += 1
            if area > max_area :
                    max_area = area
        return max_area