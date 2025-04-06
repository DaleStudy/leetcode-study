"""
Problem: 217. Contains Duplicate  

Constraints:
- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9

Time Complexity: O(n)
- 배열을 한 번만 순회함
- 집합에서 검색과 추가 연산은 평균적으로 O(1)
- 총 n개 요소에 대해 각각 O(1) 연산 수행

Space Complexity: O(n)
- 최악의 경우 모든 요소를 집합에 저장
- 추가 공간이 입력 배열 크기에 비례함
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False
