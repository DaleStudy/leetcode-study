class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        /**
        1. understanding
        - check if s's segments are all in wordDict.
        - wordDict can be used multiple times
        2. strategy
        a) dynamic programming 
        - dp[k]: substring(0,k+1) can be constructed by wordDict.
        - dp[0]: false
        - dp[1]: substring(0, 2) in wordDict
        - dp[k+1] = substring(0, k+2) in wordDict || Any(dp[k] && substring(k+1, k+2) in wordDict)
        - return dp[s.length()]
        3. complexity
        - time: O(N^2 * S), where N is the length of s, S is search time each segment in wordDict. You can calculate S in O(1) time, when change wordDict to Set. so O(N) is final time complexity.
        - space: O(N + W), W is the size of wordDict
        */
        Set<String> bow = new HashSet<>(wordDict);
        boolean[] dp = new boolean[s.length() + 1];

        for (int i = 1; i < dp.length; i++) { // O(N)
            String segment = s.substring(0, i);
            dp[i] = bow.contains(segment);
            for (int j = 0; j < i; j++) { // O(N)
                if (dp[i]) break;
                segment = s.substring(j, i);
                dp[i] = dp[i] || (dp[j] && bow.contains(segment)); // O(1)
            }
        }

        return dp[s.length()];
    }
}

