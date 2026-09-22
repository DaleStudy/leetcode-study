"""
Time Complexity: O(n)
    - n = number of elements in height
    - Each index is visited at most once by either the left or right pointer.

Space Complexity: O(1)
    - Only a small constant number of variables are used (left, right, ans).

Approach:
    - Initialize two pointers at the beginning (left) and end (right) of the array.
    - At each step, compute the area formed by the lines at left and right.
    - Update the maximum area found so far.
    - Move the pointer pointing to the shorter line inward (increase left or decrease right).
      - Ensure to move shorter line inward to potentially find a taller line that could increase the area.
      - Because amount of water is determined by the shorter line.
    - Continue until the two pointers meet.
    - Return the maximum area found.
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        N = len(height)
        left, right = 0, N - 1
        ans = 0

        while left < right:
            ans = max(ans, min(height[left], height[right]) * (right - left))

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return ans
