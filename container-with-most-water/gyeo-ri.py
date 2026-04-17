"""
[결과 요약]
# 시도한 로직 수: 3
    1. 모든 결과룰 순회하면서 시간복잡도 O(n^2)을 시도 -> LeetCode에서 Time Limit Exceed 발생
    2. 리스트 양쪽 끝에서 포인터를 이동하는 알고리즘: 시간/공간 모두 O(n)
    3. (2)의 로직은 유지한 채로 코드 가독성을 개선(알고리즘의 흐름을 쉽게 이해할 수 있도록)
"""


class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            left_height, right_height = height[left], height[right]
            min_height = min(left_height, right_height)
            width = right - left

            current_area = width * min_height
            max_area = max(max_area, current_area)

            if left_height < right_height:
                left += 1
            else:
                right -= 1

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
