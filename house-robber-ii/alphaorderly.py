"""
시간복잡도: O(n)
  - n: 입력된 배열 nums의 길이
공간복잡도: O(n)
  - n: DP 리스트(first, second)의 크기

집이 원형이라 첫 집과 마지막 집을 동시에 털 수 없으므로,
두 구간으로 나누어 각각 선형 House Robber를 적용합니다.

first는 마지막 집을 제외한 구간(0 ~ n-2),
second는 첫 집을 제외한 구간(1 ~ n-1)의 최대 금액을 저장합니다.

두 구간의 마지막 값 중 더 큰 값을 반환합니다.
"""
class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) <= 2:
            return max(nums)

        first = [nums[0], max(nums[0], nums[1])]
        second = [0, nums[1]]

        for i in range(2, len(nums)):
            if i != len(nums) - 1:
                first.append(max(nums[i] + first[i - 2], first[i - 1]))
            second.append(max(nums[i] + second[i - 2], second[i - 1]))

        return max(first[-1], second[-1])
