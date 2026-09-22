class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        max_amount = 0

        while i < j:
            left_height = height[i]
            right_height = height[j]

            amount = min(left_height, right_height) * (j - i)
            if amount > max_amount:
                max_amount = amount

            if left_height > right_height:
                j -= 1
            else:
                i += 1

        return max_amount
