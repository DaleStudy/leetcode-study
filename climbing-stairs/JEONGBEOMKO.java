package week02.Climbing_stairs;

class Solution {
    public int climbStairs(int n) {

        if (n == 1 || n == 2) {
            return n;
        }

        int[] cases = new int[n + 1];
        cases[1] = 1;
        cases[2] = 2;
        for (int i = 3; i <= n; i++) {
            cases[i] = cases[i - 1] + cases[i - 2];
        }

        return cases[n];
    }
}
