/**
 * 문자열 s가 주어질 때 wordDict의 단어 문자열로 s가 구성될 수 있는지 여부를 반환하세요.
 */
class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        int n = s.length();
        boolean[] dp = new boolean[n + 1];
        dp[0] = true;

        // contains 최적화를 위해 Set 선언: 시간 복잡도: O(n^2)
        Set<String> wordSet = new HashSet<>(wordDict);

        for (int i = 1; i <= n; i++) {
            for (int j = 0; j < i; j++) {
                String word = s.substring(j, i);
                if (dp[j] && wordSet.contains(word)) {
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[n];
    }
}

