/**
[문제풀이]
- startsWith으로 있으면 substring하면서 반복해보자.
- 주어진 list를 map으로 활용
- failed
    s = "cars"
    wordDict = ["car","ca","rs"]
    ---
    class Solution {
        public boolean wordBreak(String s, List<String> wordDict) {
            for (String word: wordDict) {
                s = s.replace(word, "");
            }
            
            if (s.length() == 0) {
                return true;
            }
            return false;
        }
    }

- DP
time: O(N^2), space: O(N)

[회고]
처음엔 너무 쉽게 생각해서 안될 것 같긴했다..
DP로 풀면 될 것 같은데..
해설을 보면 이해가 되지만, 항상 DP 접근이 잘 안된다..
 */
class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        // "applepenapple", ["apple","pen"]
        int sLen = s.length();
        boolean[] dp = new boolean[sLen + 1];
        dp[0] = true;

        int maxLen = 0;
        for (String word: wordDict) {
            maxLen = Math.max(maxLen, word.length());
        } // 5

        for (int i = 1; i <= sLen; i++) { // 1 ~ 13
            // applepenapple > apple > 5
            for (int j = i - 1; j >= 0; j--) {
                // applepenapple > apple > index:4 > 0
                if (dp[j] && wordDict.contains(s.substring(j, i))) {
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[sLen];
    }
}

