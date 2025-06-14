# https://leetcode.com/problems/missing-number/

from typing import List

class Solution:
    def missingNumber_math(self, nums: List[int]) -> int:
        """
        [Complexity]
            - TC: O(n) (sum(nums))
            - SC: O(1)

        [Approach]
            수학적으로 생각해보면, missing number는 (0 ~ n까지 값의 합) - (nums의 합)이 된다.
        """
        # (sum of [0, n]) - (sum(nums))
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)

    def missingNumber(self, nums: List[int]) -> int:
        """
        [Complexity]
            - TC: O(n)
            - SC: O(1)

        [Approach]
            bit manipulation 관점으로 접근해보면, missing number를 제외한 나머지 값은 다음 두 가지 경우에서 모두 발견된다.
                (1) 0 ~ n까지의 값
                (2) nums의 원소
            missing number는 이 두 가지 케이스 중 (1)에서만 한 번 발견되므로, 이를 XOR 연산으로 검출해 낼 수 있다.
            (짝수 번 등장한 값은 사라짐)
        """

        res = 0

        # (1) 0 ~ n까지의 값 XOR
        for i in range(len(nums) + 1):
            res ^= i
        # (2) nums의 원소 XOR
        for n in nums:
            res ^= n

        return res
