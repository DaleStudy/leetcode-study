"""
Constraints:
- 1 <= nums.length <= 2 * 10^4
- -10 <= nums[i] <= 10
- The product of any subarray of nums is guaranteed to fit in a 32-bit integer.

Time Complexity: O(n)
- 배열을 한 번만 순회하고, 각 위치에서 상수 시간 연산(max, min, 곱셈)만 수행

Space Complexity: O(1)
- 입력 크기와 무관하게 고정된 변수(curr_max, curr_min, result, temp)만 사용

풀이방법:
1. DP로 각 위치에서 가능한 최대값과 최소값을 함께 업데이트함
2. 각 위치에서 세 개의 선택지 존재: 새로 시작 vs 이전 최대값과 곱하기 vs 이전 최소값과 곱하기
3. 최소값을 계속 업데이트 하는 이유: 음수*음수 = 새로운 최대값, curr_max 업데이트할 때 쓰임 (예시: nums = [2, 3, -2, 4, -1])
4. 매 단계마다 result 업데이트

고려사항:
1. 값이 0인 경우 새로 시작해야 함
2. temp 변수: curr_min 계산 시 curr_max를 업데이트하기 전의 값이 필요함
"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max = nums[0]
        curr_min = nums[0]
        result = nums[0]
        
        for i in range(1, len(nums)):
            temp = curr_max
            curr_max = max(nums[i], curr_max * nums[i], curr_min * nums[i])
            curr_min = min(nums[i], temp * nums[i], curr_min * nums[i])
            result = max(result, curr_max)
            
        return result
