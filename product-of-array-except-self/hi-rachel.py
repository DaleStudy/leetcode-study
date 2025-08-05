"""
https://leetcode.com/problems/product-of-array-except-self/description/

문제: 정수 배열 nums가 주어졌을 때, 각 원소를 제외한 나머지 원소들의 곱을 반환하세요.
단, 나누기 연산을 사용하지 말고 O(n) 시간 복잡도로 해결하세요.

핵심 아이디어:
각 원소를 기준으로:
- 왼쪽에 있는 원소들의 곱
- 오른쪽에 있는 원소들의 곱
을 각각 곱해주면, 자기 자신을 제외한 전체 곱이 된다.

예시: [1, 2, 3, 4]
- 인덱스 0: 왼쪽(없음) × 오른쪽(2×3×4) = 24
- 인덱스 1: 왼쪽(1) × 오른쪽(3×4) = 12  
- 인덱스 2: 왼쪽(1×2) × 오른쪽(4) = 8
- 인덱스 3: 왼쪽(1×2×3) × 오른쪽(없음) = 6

TC: O(n) - 배열을 두 번 순회
SC: O(1) - 결과 배열을 제외한 추가 공간 사용하지 않음
"""

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n  # 결과 배열 초기화

        # 1단계: 왼쪽에서 오른쪽으로 순회하며 왼쪽 원소들의 곱 계산
        left_product = 1
        for i in range(n):
            result[i] = left_product  # 현재 위치에 왼쪽 곱 저장
            left_product *= nums[i]   # 다음을 위해 현재 원소 곱하기

        # 2단계: 오른쪽에서 왼쪽으로 순회하며 오른쪽 원소들의 곱 계산
        right_product = 1
        for i in range(n - 1, -1, -1):
            result[i] *= right_product  # 기존 왼쪽 곱에 오른쪽 곱 곱하기
            right_product *= nums[i]    # 다음을 위해 현재 원소 곱하기

        return result
