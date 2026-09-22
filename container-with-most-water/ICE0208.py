class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1

        most_water_size = 0
        while (left < right):
            left_h, right_h = height[left], height[right]

            current_size = (right-left) * min(left_h, right_h)
            most_water_size = max(most_water_size, current_size)

            if left_h < right_h:
                left += 1
            else:
                right -= 1
        

        return most_water_size
