class Solution:
    # 시간복잡도: O(N)
    # 공간복잡도: O(1)
    # 이 문제는 마지막 테케가 통과하지 않아서 답을 참고했습니다.
    def canJump(self, nums: List[int]) -> bool:

        gas = 0
        for n in nums:
            if gas < 0:
                return False
            elif n > gas:
                gas = n
            gas -= 1

        return True
