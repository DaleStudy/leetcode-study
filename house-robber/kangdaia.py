class Solution:
    def rob(self, nums: list[int]) -> int:
        """
        연속된 집을 훔치지 않고 최대한 많은 돈을 훔치는 함수
        
        방법
        1. DP 방식으로, 각 집을 훔칠 때의 최대 돈의 양을 업데이트 하는 방법.
            dp[0], dp[1]를 초기화 하고, dp[2]는 dp[0]+nums[2]로 구성
            이후 dp[i]는 dp[i-2]와 dp[i-3] 중 큰 값에 nums[i]를 더한 값으로 구성
            max(dp)로 최대값 찾기
        2. 1번 방법에서 점화식을 좀 더 간단하게, dp[i]는 dp[i-1]과 dp[i-2]+nums[i] 중 큰 값으로 구성하는 방법.
            dp[i-1]은 i번째 집을 훔치지 않았을 때의 최대값, dp[i-2]+nums[i]는 i번째 집을 훔쳤을 때의 최대값이므로, 둘 중 큰 값을 dp[i]로 업데이트 하는 방식.
            dp[-1]이 최대값이므로, max(dp) 대신 dp[-1]로 최대값 찾기
        3. 2번 방법에서 dp 리스트 대신, 두 개의 변수로 이전 두 집을 훔쳤을 때의 최대값을 업데이트 하는 방법.

        Args:
            nums (list[int]): 각 집에 있는 돈의 양이 담긴 리스트

        Returns:
            int: 최대로 훔칠 수 있는 돈의 양
        """
        if len(nums) <= 2:
            return max(nums)
        prev1, prev2 = 0, 0
        for num in nums:
            temp = prev1
            prev1 = max(prev1, prev2 + num)
            prev2 = temp
        return prev1
