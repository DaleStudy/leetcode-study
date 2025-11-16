class Solution {
    // Problem:
    // * can take 1 or 2 steps
    // * return: how many distinct ways to climb to the top(n)
    // Solution:
    // * Time Complexity: O(N)
    //   * due to memoization(DP)
    // * Space Complexity: O(N)
    public int climbStairs(int n) {
        // memo[i] = distinct steps to reach ith step
        int[] memo = new int[n + 1];
        memo[0] = 1;
        memo[1] = 1;

        for(int i = 2; i < n+1; i++) {
            memo[i] = memo[i-1] + memo[i-2];
        }

        return memo[n];
    }
}