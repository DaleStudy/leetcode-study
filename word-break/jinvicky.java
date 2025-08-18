import java.util.*;

class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        int n = s.length();
        boolean[] dp = new boolean[n + 1];
        dp[0] = true; // 빈 문자열은 항상 가능

        for (int i = 0; i < n; i++) {
            if (!dp[i]) continue; // 여기까지 못 오면 확장 불가
            for (String w : wordDict) {
                int j = i + w.length();
                if (j <= n && s.startsWith(w, i)) {
                    dp[j] = true;
                }
            }
        }
        return dp[n];
    }
}
