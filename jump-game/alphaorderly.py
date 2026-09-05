"""
시간복잡도: O(n)
공간복잡도: O(1)

- 현재 위치(index)에서 갈 수 있는 가장 먼 위치(furthest)를 갱신한다.
- furthest가 현재 위치보다 작으면 도달할 수 없으므로 False를 반환한다.
- 갱신된 furthest가 마지막 인덱스 이상이 되면 True를 반환한다.
"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        furthest = 0

        for index, jump in enumerate(nums):
            if furthest < index:
                return False

            furthest = max(furthest, index + jump)
            if furthest >= N - 1:
                return True

        return False
