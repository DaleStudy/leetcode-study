class Solution {

    public int climbStairs(int n) {
        int[] ans = new int[n + 1];
        if (n <= 2) {
            return n;
        }
        ans[1] = 1;
        ans[2] = 2;

        for (int i = 3; i < n + 1; i++) {
            ans[i] = ans[i - 1] + ans[i - 2];
        }
        return ans[n];
    }
}
/**
 * TC: O(N)
 * SC: O(N)
 */
