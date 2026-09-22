import java.util.*;

// n = s.length(), m = wordDict.size(), L = 사전 단어의 최대 길이
// TC: O(n * m * L)
// SC: O(n)
class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        int n = s.length();

        // dp[i] = 인덱스 i부터 시작하는 뒷부분을 사전 단어로 빈틈없이 쪼갤 수 있는가
        boolean[] dp = new boolean[n + 1];
        dp[n] = true;

        // dp[i]는 자기보다 오른쪽의 dp[i + word.length()]를 참조하므로 뒤에서 앞으로 채운다
        for (int i = n - 1; i >= 0; i--) {
            for (String word : wordDict) {
                // startsWith(word, i)는 substring 없이 i번째부터 비교한다
                if (s.startsWith(word, i) && dp[i + word.length()]) {
                    dp[i] = true;
                    break;
                }
            }
        }

        return dp[0];
    }
}

// 첫 번째 풀이 — top-down 재귀 + 메모이제이션 (TC: O(n^2 * m), SC: O(n^2))
// 남은 뒷부분을 문자열 그대로 메모 key로 써서 substring으로 새 문자열을 만들고 그 문자열을 n개까지 저장한다.
//
// public boolean wordBreak(String s, List<String> wordDict) {
//     return dfs(s, wordDict, new HashMap<>());
// }
//
// private boolean dfs(String s, List<String> wordDict, Map<String, Boolean> memo) {
//     if (s.isEmpty()) return true;
//     if (memo.containsKey(s)) return memo.get(s);
//
//     for (String word : wordDict) {
//         if (s.startsWith(word)) {
//             if (dfs(s.substring(word.length()), wordDict, memo)) {
//                 memo.put(s, true);
//                 return true;
//             }
//         }
//     }
//
//     memo.put(s, false);
//     return false;
// }
