class Solution {

    public int climbStairs(int n) {
        if (n == 1) {
            return n;
        }
        int a1 = 1;
        int a2 = 2;
        for (int i = 3; i < n + 1; i++) {
            int a3 = a1 + a2;
            a1 = a2;
            a2 = a3;
        }
        return a2;
    }
}
/**
 * TC: O(N)
 * SC: O(1)
 */
