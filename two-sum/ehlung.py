"""
n = nums의 길이
시간 복잡도: O(n) - 각 숫자를 한 번씩 확인 (딕셔너리 조회/저장은 O(1))
공간 복잡도: O(n) - 숫자와 인덱스를 담는 딕셔너리
"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        index_of = {}
        for i, num in enumerate(nums):
            need = target - num
            if need in index_of:
                return [index_of[need], i]
            index_of[num] = i
        return []
