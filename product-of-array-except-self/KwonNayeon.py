"""
Constraints:
  1. 2 <= nums.length <= 10^5
  2. -30 <= nums[i] <= 30
  3. The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer

Time Complexity: O(n)
  - 배열을 두 번 순회하므로 O(n)

Space Complexity: O(1)
  - 출력 배열(answer)을 제외하면 추가 공간이 상수만큼만 필요(left, right 변수)

풀이 방법:
  1. answer 배열을 1로 초기화 (곱셈에서는 1이 영향을 주지 않음)
  2. 왼쪽에서 오른쪽으로 순회:
     - answer[i]에 현재까지의 left 누적값을 곱함
     - left *= nums[i]로 다음을 위해 left 값을 업데이트
  3. 오른쪽에서 왼쪽으로 순회 (range(n-1, -1, -1) 사용):
     - answer[i]에 현재까지의 right 누적값을 곱함
     - right *= nums[i]로 다음을 위해 right 값을 업데이트
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        left = 1
        for i in range(n):
            answer[i] *= left
            left *= nums[i]

        right = 1
        for i in range(n-1, -1, -1):
            answer[i] *= right
            right *= nums[i]
    
        return answer
