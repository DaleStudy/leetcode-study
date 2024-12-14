import java.util.Arrays;

class Solution {
    int size = 0;
    int[] numArray;
    int[] dp;

    public int rob(int[] nums) {
        size = nums.length;
        dp = new int[size];
        // 배열의 모든 값을 -1로 변경
        Arrays.fill(dp, -1);
        numArray = nums;
        return fun(0);
    }

    private int fun(int idx) {
        if (idx >= size) return 0;
        if (dp[idx] != -1) return dp[idx];
        dp[idx] = 0; // check
        dp[idx] += Math.max(fun(idx + 2) + numArray[idx], fun(idx + 1));
        return dp[idx];
    }
}