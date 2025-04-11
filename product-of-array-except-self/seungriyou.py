# https://leetcode.com/problems/product-of-array-except-self/

from typing import List

class Solution:
    def productExceptSelf1(self, nums: List[int]) -> List[int]:
        """
        [Complexity]
            - TC: O(n)
            - SC: O(n)

        [Approach]
            division operation 없이 각 원소마다 자기 자신을 제외한 모든 값의 곱을 구해야하므로, 다음의 순서로 수행할 수 있다.
                1) 왼쪽 방향으로 순회하면서 각 원소보다 왼쪽에 있는 값들의 곱으로 left 배열 채우기
                2) 오른쪽 방향으로 순회하면서 각 원소보다 오른쪽에 있는 값들의 곱으로 right 배열 채우기
                3) left와 right 배열의 원소마다 곱을 구해서 결과 배열 반환하기
        """
        n = len(nums)

        left = [1] * n
        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]

        right = [1] * n
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        return [l * r for l, r in zip(left, right)]

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        [Complexity]
            - TC: O(n)
            - SC: O(n) (O(1) extra space)

        [Approach]
            follow up 조건을 위해서는 첫 번째 풀이처럼 left, right 배열을 두면 안 되고, res 배열에서 값을 업데이트 해나가야 한다.
            이때, O(1) space를 위해서 변수 prev를 사용하여, 순회 진행 방향 기준 이전 값들의 곱을 트래킹해나가면 된다.
                1) nums를 왼쪽 방향으로 순회하면서 res 및 prev 값 업데이트
                2) nums를 오른쪽 방향으로 순회하면서 res 및 prev 값 업데이트
        """
        n = len(nums)
        res = []

        prev = 1
        for i in range(n):
            res.append(prev)
            prev *= nums[i]

        prev = 1
        for i in range(n - 1, -1, -1):
            res[i] *= prev
            prev *= nums[i]

        return res
