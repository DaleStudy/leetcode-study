import java.util.*;

// TC: O(n)
// SC: O(n)
class Solution {
    public int numDecodings(String s) {
        int n = s.length();
        int[] dp = new int[n + 1];
        dp[n] = 1;

        for (int i = s.length() - 1; i >= 0; i--) {
            if (s.charAt(i) != '0') {
                dp[i] = dp[i + 1];
            }
            if (i + 1 < n) {
                int twoDigit = Integer.parseInt(s.substring(i, i + 2));
                if (twoDigit >= 10 && twoDigit <= 26) {
                    dp[i] += dp[i + 2];
                }
            }
        }
        return dp[0];
    }
}
