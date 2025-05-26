"""
Constraints:
- 1 <= nums.length <= 2 * 10^4
- -10 <= nums[i] <= 10
- The product of any subarray of nums is guaranteed to fit in a 32-bit integer.

Time Complexity: O(n)
- 배열을 한 번만 순회하면서 각 위치에서 상수 시간 연산만 수행

Space Complexity: O(1)
- 고정된 추가 변수만 사용 (curr_max, curr_min, ...)

풀이방법:
1. DP로 각 위치에서 가능한 최대곱과 최소곱을 동시에 추적함
2. 각 위치에서 세 개의 선택지 존재: 새로 시작 vs 이전 최대곱과 곱하기 vs 이전 최소곱과 곱하기
3. 최소곱이 필요한 이유: 나중에 음수를 만났을 때 최대값이 될 수 있기 때문
4. 매 단계마다 result 업데이트

고려사항:
1. 값이 0인 경우 → 새로 시작해야 함
2. temp 변수: curr_max를 업데이트하면 curr_min 계산 시 원래 값이 필요함
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

