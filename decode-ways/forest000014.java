/*
# Time Complexity: O(n)
# Space Complexity: O(n)
*/
class Solution {

    private boolean check12(char ch) {
        return (ch == '1' || ch == '2');
    }

    private boolean check1(char ch) {
        return ch == '1';
    }

    private boolean check2(char ch) {
        return ch == '2';
    }

    private boolean check0(char ch) {
        return ch == '0';
    }

    private boolean check6(char ch) {
        return ch <= '6';
    }

    public int numDecodings(String s) {
        int n = s.length();

        if (n == 0)
            return 0;

        int[] dp = new int[n + 1];

        if (check0(s.charAt(0)))
            return 0;

        dp[0] = 1;
        dp[1] = 1;
        if (n == 1)
            return dp[1];

        for (int i = 1; i < n; i++) {
            if (check0(s.charAt(i)) && !check12(s.charAt(i - 1)))
                return 0;

            if (!check0(s.charAt(i)))
                dp[i + 1] = dp[i];

            if (check1(s.charAt(i - 1)) || (check6(s.charAt(i)) && check2(s.charAt(i - 1))))
                dp[i + 1] += dp[i - 1];
        }
        return dp[n];
    }
}
