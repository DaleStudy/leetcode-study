class Solution:
    """
    Solution 1:
        뒤에서 부터 푸는 방법이 있을거라 생각했습니다.
        풀이는 성공했지만 성능은 느린 5% 라는 느린 성능을 보입니다.

    Time: O(n * 10^5) - 10^5 는 nums 원소의 최대 값
    Space: O(n)
    """

    def canJump(self, nums: List[int]) -> bool:
        dp = [False for i in range(len(nums))]

        dp[len(nums) - 1] = True

        for i in range(len(nums) - 1 - 1, -1, -1):
            for j in range(1, nums[i] + 1):
                if i + j < len(nums) and dp[i + j]:
                    dp[i] = True
                    break

        return dp[0]

    """
    Solution 2:
        Greedy - 솔루션을 참고했습니다.

    Time: O(n)
    Space: O(1)
    """

    def canJump(self, nums: List[int]) -> bool:
        reach = 0
        for idx in range(len(nums)):
            if idx <= reach:
                reach = max(reach, idx + nums[idx])
        return reach >= len(nums) - 1
