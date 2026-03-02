from typing import List


class Solution:
    """
    풀이:
    - nums를 set으로 변환하면 중복이 제거된다.
    - set의 길이와 원본 리스트의 길이가 다르면 중복이 존재한다는 뜻.

    TC: O(n)
      - set(nums): 리스트의 모든 원소를 순회하면서 set에 삽입. O(n)
        - set 삽입은 해시 기반이라 평균 O(1), n개 원소니까 O(n)
      - len(set(nums)): set의 길이 조회. O(1)
      - len(nums): 리스트의 길이 조회. O(1)
      - 종합: O(n) + O(1) + O(1) = O(n)

    SC: O(n)
      - set(nums): 중복이 없는 경우 최대 n개의 원소를 저장. O(n)
      - 그 외 변수 없음
    """
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
