class Solution {
    // TC: O(n)
    // SC: O(1)
    public int climbStairs(int n) {
        if (n < 3) {
            // If n is less than 3 there are n ways.
            return n;
        }

        // There is one way to reach the first stair.
        int nMinus2 = 1;
        // There are two ways to reach the second stair.
        int nMinus1 = 2;

        int nZero = nMinus1 + nMinus2;

        for (int step = 3; step <= n; step++) {
            // To reach the third stair, it must come from the first stair or the second
            // stair.
            // The number of ways to reach the nth stair is the sum of those of the (n-1)th
            // stair and those of the (n-2)th stair.
            nZero = nMinus1 + nMinus2;

            nMinus2 = nMinus1;
            nMinus1 = nZero;
        }

        // A separate variable name is used to distinguish between nZero and nMinus1 so
        // that the nth value is explicit
        return nZero;
    }
}
