class Solution:
    """
        - 이전 풀이
        [1,2,3,1]
        인덱스 0에서 훔쳤을 때, 인덱스 1은 훔치면 안되므로 nums[0] + F(nums[2:])
        인덱스 0에서 안훔쳤을 때, 인덱스 1에서 훔쳐야 하므로 F(nums[1:])
        
        F[nums] = max(nums[0] + F[nums[2:]], F(nums[1:]))
        F[i] = max(nums[i] + F(i+2), F(i+1))


        - dp
        nums = [1, 2, 3, 1]
        집이 하나일 때는 한 곳만 볼 수 있으니 그 집의 돈을 훔침: dp[0] = nums[0] = 1
        집이 두 개일 때, 인덱스 0인 곳을 갔다면 dp[0]이 가장 크고,
        가지 않았다면 인덱스 1을 가게 됨. dp[1] = max(dp[0], nums[1]) = max(1, 2) = 2
        그래서 인덱스 0을 갔을 때와 가지 않았을 때를 고려하여 큰 돈을 가져옴
        집이 세 개일 때, 인덱스 0을 갔다면 인덱스 2를 가야하고, 인덱스 0을 가지 않았다면 인덱스 1을 감
        이를 고려하면, 인덱스 0을 갔을 때의 가장 큰 값이 dp[0]이고, 인덱스 2를 가야하니 nums[2]를 더한 값과
        인덱스 0에 가지 않고 인덱스 1로 갔다면 dp[1]이 가장 크다.
        그래서 dp[2] = max(dp[0] + nums[2], dp[1])
        집이 네 개일 때, 인덱스 3을 간다면 인덱스 1을 가게 되므로 인덱스 1까지의 dp 값과 인덱스 3의 값을 더한 값과
        인덱스 3을 가지 않는다면 인덱스 0과 인덱스 2를 가게 된다.
        그렇다면 인덱스 2까지의 값을 비교하여 더 큰 돈을 가져간다.
        그래서 dp[3] = max(dp[1] + nums[3], dp[2])가 된다.

        - TC
            - for loop -> O(n)
        - SC
            - dp 테이블 크기 -> O(n)
    """
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        
        return dp[-1]
