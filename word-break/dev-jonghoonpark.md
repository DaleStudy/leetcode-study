- 문제: https://leetcode.com/problems/word-break/
- 풀이: https://algorithm.jonghoonpark.com/2024/02/28/leetcode-139

```java
class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        boolean[] dp = new boolean[s.length() + 1];
        dp[0] = true;

        for (int i = 1; i <= s.length(); i++) {
            for (String word : wordDict) {
                if (i >= word.length()) {
                    int start = i - word.length();
                    if (dp[start] && s.startsWith(word, start)) {
                        dp[i] = true;
                    }
                }
            }
        }

        return dp[s.length()];
    }
}
```

### TC, SC

s의 길이를 n 이라 하고, wordDict의 크기를 m 이라고 할 때, 시간복잡도는 `O(n * m)` 공간복잡도는 `O(n)` 이다.
