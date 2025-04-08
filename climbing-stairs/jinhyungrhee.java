import java.util.*;
class Solution {
    public int climbStairs(int n) {

        // METHOD1 : recursive DFS
        // int resuslt = recursiveDFS(0, n);

        // METHOD2 : recursive DFS + memoization
        // int[] memo = new int[n + 1];
        // Arrays.fill(memo, -1);
        // int result = memoizationDFS(0, n, memo);

        // METHOD3 : DP
        int[] memo = new int[n + 1];
        Arrays.fill(memo, -1);
        int result = dp(n, memo);

        return result;
    }

    /**
     runtime : 0ms
     memory : 40.04mb
     */

    // METHOD3 : DP (Bottom-Up)
    // time-complexity : O(N)
    // space-complexity : O(N)
    public int dp(int n, int[] memo) {
        if (n <= 2) return n;
        memo[1] = 1;
        memo[2] = 2;
        for (int i = 3; i < n + 1; i++) {
            memo[i] = memo[i - 1] + memo[i - 2];
        }
        return memo[n];
    }

    /**
     runtime : 0ms
     memory : 40.30mb
     */

    // METHOD2 : DFS + memoization (Top-Down)
    // time-complexity : O(N) -> 각 i에 대해 dfs(i)는 최대 한번만 호출됨
    // space-complexity : O(N)
    public int memoizationDFS(int i, int n, int[] memo) {
        if (i > n) return 0;
        if (i == n) return 1;
        if (memo[i] != -1) return memo[i];
        memo[i] = memoizationDFS(i + 1 , n, memo) + memoizationDFS(i + 2, n, memo);
        return memo[i];
    }

    /**
     Time Limit Exceeded
     */

    // METHOD1 : recursive DFS => TIME-OUT 발생
    // time-complexity : O(2^N) -> n이 커질수록 중복 호출 발생
    // space-complexity : O(N)
    public int recursiveDFS(int i, int n) {
        if (i > n) return 0;
        if (i == n) return 1;
        return recursiveDFS(i + 1, n) + recursiveDFS(i + 2, n);
    }
}