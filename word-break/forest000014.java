/*

Time Complexity: O(s * L^2)
    - L is max length of wordDict[i]
Space Complexity: O(s + w * L)
*/
class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        Set<String> wordSet = new HashSet<>();
        int maxLen = 0;
        for (String word : wordDict) {
            wordSet.add(word);
            maxLen = Math.max(maxLen, word.length());
        }

        boolean[] dp = new boolean[s.length() + 1];
        dp[0] = true;

        for (int i = 0; i < s.length(); i++) {
            for (int j = 1; j <= maxLen; j++) {
                int beginIdx = i - j + 1;
                if (beginIdx < 0)
                    continue;
                if (wordSet.contains(s.substring(beginIdx, i + 1)) && dp[beginIdx]) {
                    dp[i + 1] = true;
                    break;
                }
            }
        }

        return dp[s.length()];
    }
}
