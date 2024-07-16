- 문제: https://leetcode.com/problems/longest-common-subsequence/
- 풀이: https://algorithm.jonghoonpark.com/2024/07/17/leetcode-1143

```java
class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        int[][] dp = new int[text1.length() + 1][text2.length() + 1];

        for (int i = 1; i < dp.length; i++) {
            for (int j = 1; j < dp[0].length; j++) {
                if (text1.charAt(i - 1) == text2.charAt(j - 1)) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                } else {
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }

        return dp[text1.length()][text2.length()];
    }
}
```

### TC, SC

시간 복잡도는 `O(m * n)` 공간 복잡도는 `O(m * n)` 이다.
