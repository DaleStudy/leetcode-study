class Solution {
    public int climbStairs(int n) {
        int result = 0;
        int first = 1;
        int second = 2;
        int third = 3;
        if (n == 1) {
            return first;
        } else if (n == 2) {
            return second;
        } else if (n == 3) {
            return third;
        }

        for (int i = 4; i <= n; i++) {
            result = second + third;
            second = third;
            third = result;
        }
        return result;
    }
}
