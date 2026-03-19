"""
[결과 요약]
# 재시도횟수: 2회
    1. 반복문으로 구하기: 로직은 쉬우나 n이 최대 10^4이므로 input 길이에 따라 속도가 느려질 수 있음
    2. 등차수열의 원리를 활용하여 n!을 구한 다음 nums의 합을 빼주기
"""


class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        len_nums = len(nums)
        total_sum = int(len_nums * (len_nums + 1) / 2)
        return total_sum - sum(nums)


if __name__ == "__main__":
    test_cases = [
        ([3, 0, 1], 2),
        ([0, 1], 2),
        ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8),
    ]

    solution = Solution()
    for idx, case_ in enumerate(test_cases):
        nums, answer = case_
        result = solution.missingNumber(nums)
        assert (
            answer == result
        ), f"Test Case {idx} Failed: Expected {answer}, Got {result}"
