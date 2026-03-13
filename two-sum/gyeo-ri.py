"""
[결과 요약]
# 재시도횟수: 3회
    1. 배열의 모든 경우의 수 계산하기
        - 시간복잡도 O(n^2)
    2. 전체 반복하지 않고 인덱스 기준 뒤만 반복하기
        - O(n^2)이지만 약간 더 효율적
    3. 딕셔너리(Map) 사용
        - 시간복잡도: O(n) / 공간복잡도: O(n)
        - 딕셔너리 자체는 빨리 떠올렸으나 Key 중복이 될 수 있다고 잘못 판단하여 시간을 오래 소모
            - 실제로 하나의 숫자는 최대 두 번까지 사용되어 구조 상 Key가 중복되지 않음
"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_dict = {}

        for idx1, num1 in enumerate(nums):
            num2 = target - num1
            idx2 = nums_dict.get(num2)

            if idx2 is None:
                nums_dict.update({num1: idx1})
            else:
                return [idx1, idx2]

        raise Exception("Invalid nums and target")


if __name__ == "__main__":
    test_cases = [
        ([2, 7, 11, 15], 9, {0, 1}),
        ([3, 2, 4], 6, {1, 2}),
        ([3, 3], 6, {0, 1}),
        ([-2, -3, 0, 3], 1, {0, 3}),
        ([0, -5, 2, 6], -3, {1, 2}),
        ([4, 7, 2, 0, 0], 0, {3, 4}),
    ]

    solution = Solution()
    for idx, case_ in enumerate(test_cases):
        nums, target, answer = case_
        result = solution.twoSum(nums, target)
        assert answer == set(
            result
        ), f"Test Case {idx} Failed: Expected {answer}, Got {result}"
