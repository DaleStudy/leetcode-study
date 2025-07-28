from typing import List

"""
문제 설명:
- 배열에 중복된 값이 하나라도 있으면 True, 아니면 False를 반환하는 문제

목표
- 배열을 순회하면서 각 값을 set에 추가
- set은 중복을 허용하지 않으므로, 이미 set에 값이 있으면 중복이 발생한 것
- 중복이 발견되면 true, 없으면 false 반환

시간복잡도: O(n)
- 배열을 한 번만 순회하므로 O(n)

공간복잡도: O(n)
- set에 n개의 값이 저장됨
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set()
        for num in nums:
            if num in num_set:
                return True
            else:
               num_set.add(num)
        return False


