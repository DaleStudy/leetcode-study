"""
https://leetcode.com/problems/3sum/

문제 설명:
정렬되지 않은 정수 배열 nums가 주어질 때, 
세 수의 합이 0이 되는 모든 유니크한 triplet을 찾는 문제.

조건:
- 중복 조합은 허용되지 않음.
- 예: [-1, 0, 1]과 [0, -1, 1]은 같은 조합이므로 하나만 포함.

풀이 전략:
1. 배열을 정렬한다.
2. 첫 번째 수를 고정한 뒤, 나머지 두 수를 투포인터로 탐색한다.
   - 합이 0보다 작으면 left를 증가
   - 합이 0보다 크면 right를 감소
   - 합이 0이면 정답에 추가, 중복 방지 처리도 함께 수행

TC: O(n^2), 정렬 O(n log n) + 투포인터 O(n^2)
SC: O(1), 출력 공간 result 제외
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # 중복 제거

            left, right = i + 1, len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                # 조건 만족시 정답에 추가
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    # 같은 값을 가진 left가 여러 개 있다면, 중복 건너뜀
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # 같은 값을 가진 right가 여러 개 있다면, 중복 건너뜀
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                # 총합이 0보다 작으면, 더 큰 수가 필요하니까 left를 오른쪽으로 이동
                elif total < 0:
                    left += 1
                # 총합이 0보다 크면, 더 작은 수가 필요하니까 right를 왼쪽으로 이동
                else:
                    right -= 1

        return result



# O(n^2) time, O(n) space
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()

        for i in range(len(nums) - 2):
            seen = set()
            for j in range(i + 1, len(nums)):
                complement = -(nums[i] + nums[j])
                if complement in seen:
                    triplet = [nums[i], nums[j], complement]
                    triplets.add(tuple(sorted(triplet)))
                seen.add(nums[j])

        return list(triplets)
