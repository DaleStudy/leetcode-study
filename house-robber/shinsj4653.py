"""
Inputs: 정수형 배열 nums

Outputs: 훔치는 돈의 max값

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 400

Time Complexity: O(2^n) X

dp[n] = max(dp(n), dp(n - 2) + nums[i])
재귀 사용
2^(100)
2^10 = 10^3
막상 실제 값을 출력하면 말이 안되는 값..

Space Complexity: O(n)
dp 배열은 nums와 똑같으므로

# 에러
constraint로 인한 반례 항상 생각하도록!
len이 0이거나 1일때는 따로 처리!

# 반례
nums =
[2,1,1,2]

output = 3, expected = 4

len(nums) - 1이 0 혹은 1일때, 즉 nums길이가 1 혹은 2일 경우엔 따로 처리

"""


class Solution:
    def rob(self, nums) -> int:
        dp = [-1 for _ in range(len(nums))]
        n = len(nums) - 1

        if n == 0:
            return nums[0]

        # 초기값 세팅
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])

        if n == 1:
            return dp[1]

        def memo(i):
            if dp[i] != -1:
                return dp[i]

            dp[i] = max(memo(i - 1), nums[i] + memo(i - 2))
            return dp[i]

        return max(memo(n - 1), nums[n] + memo(n - 2))

