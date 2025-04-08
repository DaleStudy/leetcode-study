class Solution {
    public int climbStairs(int n) {
        int[] memo = new int[n + 1];
        return recur(n, memo);
    }

    int recur(int n, int[] memo) {
        if (n < 0) {
            return 0;
        }

        if (n == 0) {
            return 1;
        }

        if (memo[n] > 0) {
            return memo[n];
        }

        memo[n] = recur(n - 1, memo) + recur(n - 2, memo);
        return memo[n];
    }
}
