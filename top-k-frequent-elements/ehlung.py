"""
n = nums의 길이, m = 서로 다른 숫자의 개수
시간 복잡도: O(n + m log m) - 빈도 세기 O(n) + 서로 다른 숫자 m개를 빈도순 정렬 O(m log m)
공간 복잡도: O(m) - 숫자별 빈도를 담는 딕셔너리와 정렬 결과
"""


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        sorted_nums = sorted(count, key=lambda num: count[num], reverse=True)
        return sorted_nums[:k]
