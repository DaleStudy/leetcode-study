"""
[문제풀이]
# Inputs
- sorted rotated array : nums
- nums안의 요소는 unique
# Outputs
- 배열의 가장 작은 값 Return
# Constraints
- O(logN) 시간대로 풀어야함
- n == nums.length
- 1 <= n <= 5000
- -5000 <= nums[i] <= 5000
- All the integers of nums are unique.
- nums is sorted and rotated between 1 and n times.
# Ideas
그냥 정렬은 O(NlogN) 이어서 불가능
rotate : 맨 끝의 요소가 맨 처음으로 옴
이진탐색이 O(logN) 이긴한데..->하지만, 이진탐색은 정렬된 배열에서만 사용가능
그리고, 이 문제에선 아닌 것 같다

끝의 원소를 빼서 stack에 append -> 모두 o(1)

회전되어 있는 배열의 특성을 활용하여
-> 끝의 원소 빼고, 그걸 stack 에 넣기
-> 그리고 stack의 맨 끝 원소보다 nums의 끝 원소가 더 클때
stack[-1] 이 정답
-> 근데 이건 o(n) 아닌가??

우선 내 풀이 정답
해설 참고
-> 내 풀이는 O(n) 이다.. O(logN) 풀이가 필요
이분탐색 응용문제이다

[회고]

"""

# 내 풀이
from collections import deque


class Solution:
    def findMin(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        nums = deque(nums)

        st = []
        ret = 0

        while nums:
            num = nums.pop()

            if not nums:
                ret = num
                break

            if num < nums[-1]:
                ret = num
                break

        return ret

# 해설
class Solution:
    def findMin(self, nums: List[int]) -> int:

        left, right = 1, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            if nums[0] < nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return nums[0]


