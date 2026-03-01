from typing import List


class Solution:
    """
    TC: O(n)
      - set(nums): n개 원소를 해시셋에 삽입, 각 삽입 평균 O(1) → O(n)
      - len()은 내부 size 필드 반환이므로 O(1)

    SC: O(n)
      - set이 최대 n개 원소를 저장
    """
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
