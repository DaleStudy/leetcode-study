class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_area = 0
        left_idx = 0
        right_idx = len(height) - 1

        while left_idx < right_idx:
            left_h = height[left_idx]
            right_h = height[right_idx]

            max_area = max(max_area, (right_idx - left_idx) * min(left_h, right_h))

            if left_h < right_h:
                left_idx += 1
            else:
                right_idx -= 1

        return max_area


if __name__ == "__main__":
    test_cases = [
        ([1, 1], 1),
        ([1, 2, 1], 2),
        ([4, 3, 2, 1, 4], 16),
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 2, 4, 3], 4),
        ([2, 3, 10, 5, 7, 8, 9], 36),
        ([1, 3, 2, 5, 25, 24, 5], 24),
        ([5, 5, 5, 5, 5], 20),
        ([1, 1000, 1, 1000, 1], 2000),
        ([1, 2, 3, 4, 5, 6], 9),
    ]

    solution = Solution()
    for idx, case_ in enumerate(test_cases):
        height, answer = case_
        result = solution.maxArea(height)
        assert (
            answer == result
        ), f"Test Case {idx + 1} Failed: Expected {answer}, Got {result}"
