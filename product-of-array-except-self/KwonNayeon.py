"""
Constraints:
- 나눗셈 연산 사용 불가능
- O(n) 시간 복잡도로 구현해야 함
- 모든 prefix/suffix 곱은 32비트 정수 범위 내에 있음

Time Complexity: O(n)
- 배열을 두 번만 순회

Space Complexity: O(1)
- 출력 배열 외 추가 공간은 상수만 사용 (left, right 변수)

풀이 방법:
- 각 위치의 결과는 (왼쪽 모든 요소의 곱) * (오른쪽 모든 요소의 곱)
- 두 번의 순회로 이를 계산:
  1. 왼쪽 -> 오른쪽: 각 위치에 왼쪽 모든 요소의 누적 곱 저장
  2. 오른쪽 -> 왼쪽: 각 위치에 오른쪽 모든 요소의 누적 곱을 곱함

예시: nums = [1, 2, 3, 4]
1단계 후: answer = [1, 1, 2, 6]
2단계 후: answer = [24, 12, 8, 6]
"""

# Final result = (product of all elements on the left side) * (product of all elements on the right side)

# Step 1: Initialize result array with 1s
# Step 2: Traverse from left to right, storing cumulative product of left side
# Step 3: Traverse from right to left, multiplying with cumulative product of right side
# nums = [1,2,3,4]
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        left = 1
        for i in range(n):
            answer[i] *= left
            left *= nums[i]
# answer = [1, 1, 2, 6] at this point
        right = 1
        for i in range(n-1, -1, -1):
            answer[i] *= right
            right *= nums[i]

        return answer
# answer = [24,12,8,6]
