public class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        boolean[] dp = new boolean[s.length() + 1];
        dp[0] = true;

        for (int n = 1; n <= s.length(); n++) {
            for (String word : wordDict) {
                if (n >= word.length() && s.substring(n - word.length(), n).equals(word)) {
                    dp[n] = dp[n - word.length()];
                }
                if (dp[n]) {
                    break;
                }
            }
        }

        return dp[s.length()];
    }
}

