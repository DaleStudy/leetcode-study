/*
dp[i] = dp[i-1] + dp[i-2]
Time Complexity : O(n)
Space Complexity : O(n)
*/
class Solution {
    public int numDecodings(String s) {
        int n = s.length();
        int[] dp = new int[n + 1];
        dp[n] = 1;

        for (int i = n-1; i > -1; i--) { 
            if (s.charAt(i) != '0') {
                dp[i] += dp[i+1];
            }
            if (s.charAt(i) != '0' && i+1 < n) {
                int twoDigit = Integer.valueOf(s.substring(i, i+2));
                if (twoDigit > 0 && twoDigit < 27) {
                    dp[i] += dp[i+2];
                }
            }
        }
        return dp[0];
    }
}
