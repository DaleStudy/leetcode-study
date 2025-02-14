"""
Constraints:
- 1 <= nums.length <= 5000
- -10^4 <= nums[i] <= 10^4
- All values of nums are unique.
- nums is an ascending array that is possibly rotated.
- -10^4 <= target <= 10^4

Time Complexity: O(log n)
- Binary Search -> 매 단계마다 탐색 범위가 절반으로 줄어듦

Space Complexity: O(1)
- 추가 공간을 사용하지 않음

풀이방법:
1. Binary Search
   - left와 right 포인터로 탐색 범위 지정
   - mid가 target인지 먼저 확인
2. 정렬된 부분 찾기
   - mid를 기준으로 왼쪽이 정렬되어 있는지 확인
   - 정렬된 부분에서 target이 존재할 수 있는 범위를 파악
3. Target 위치 탐색
   - 왼쪽이 정렬되어 있고 target이 그 범위 안에 있다면 오른쪽 범위를 줄임
   - 그렇지 않다면 왼쪽 범위를 늘림
   - 반대의 경우도 동일한 방법 적용
4. Target을 찾지 못한 경우 -1을 반환함
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1

