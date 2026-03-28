class Solution {
    // TC : O(n)
    // SC : O(1)
    public int numDecodings(String s) {
        // If it starts with 0, the value can't be decoded.
        if (s.charAt(0) == '0') {
            return 0;
        }

        int n = s.length();

        int prev2 = 1;
        int prev1 = 1;

        // dp[i] = dp[i-1] + dp[i-2]
        for (int i = 1; i < n; i++) {
            int current = 0;

            if (s.charAt(i) != '0') {
                current += prev1;
            }

            int twoDigit = Integer.valueOf(s.substring(i - 1, i + 1));

            if (twoDigit >= 10 && twoDigit <= 26) {
                current += prev2;
            }

            prev2 = prev1;
            prev1 = current;
        }

        return prev1;
    }
}
