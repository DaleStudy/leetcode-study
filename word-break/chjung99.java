class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        Set<String> wordSet = new HashSet<>(wordDict);
        int n = s.length();
        boolean[] dp = new boolean[n];
        for (int i = 0; i < n; i++) {
            dp[i] = wordSet.contains(s.substring(0, i+1));
            for (int j = 0; j < i; j++) {
                if (dp[j] && wordSet.contains(s.substring(j+1, i+1))){
                    dp[i] = true;
                }
            }
        }

        return dp[n-1];
    }
}


