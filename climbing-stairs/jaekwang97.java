class Solution {
    public int climbStairs(int n) {
        if (n <= 2) return n;

        int prev = 1;
        int cur = 2;

        for (int i = 3; i <= n; i++) {
            int next = prev + cur;
            prev = cur;
            cur = next;
        }

        return cur;
    }
}
