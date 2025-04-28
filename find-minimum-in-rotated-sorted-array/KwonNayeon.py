"""
Input/Output/Constraints:
- Input: A rotated sorted array (e.g., [4,5,6,7,0,1,2])
- Output: The minimum element in the array (e.g., 0)
- Constraints: Algorithm must run in O(log n) time

Time Complexity: O(log n) 
- 이진 탐색을 사용하므로 매 단계마다 탐색 범위가 절반으로 줄어듦

Space Complexity: O(1)
- 추가 공간을 사용하지 않고 포인터만 사용

풀이방법:
1. 이진 탐색(Binary Search) 활용
2. mid와 right 값을 비교하여 조건을 나눔
  - Case 1: nums[mid] > nums[right]
    - 최솟값은 mid 오른쪽에 존재
    - left = mid + 1
  - Case 2: nums[mid] <= nums[right]
    - 최솟값은 mid를 포함한 왼쪽에 존재 가능
    - right = mid
3. Pivot이 일어난 지점의 값을 반환
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            
            else:
                right = mid
        
        return nums[left]
