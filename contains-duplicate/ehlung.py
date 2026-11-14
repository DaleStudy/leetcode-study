"""
n = nums의 길이
시간 복잡도: O(n) - 각 숫자를 한 번씩 확인 (set 조회/추가는 O(1))
공간 복잡도: O(n) - 지금까지 본 숫자들을 담는 set
"""


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
