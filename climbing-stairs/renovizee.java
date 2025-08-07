


// tag renovizee 2week
// https://github.com/DaleStudy/leetcode-study/issues/230
// https://leetcode.com/problems/climbing-stairs/ #70 #Easy
class Solution {
    // Solv1
    // 시간복잡도 : O(n)
    // 공간복잡도 : O(n)
    public int climbStairs(int n) {
        int[] dp = new int[]{1, 2};

        if (n == dp[0]) {
            return dp[0];
        }

        if (n == dp[1]) {
            return dp[1];
        }

        for (int i = 3; i <= n; i++) {
            int nextWayCount = dp[0] + dp[1];
            dp[0] = dp[1];
            dp[1] = nextWayCount;
        }

        return dp[1];

    }
}
//-------------------------------------------------------------------------------------------------------------
// Java 문법 피드백
// 1) Math.pow(2, 3) 2의 3승.
//-------------------------------------------------------------------------------------------------------------
