import java.util.*;

class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        int n = s.length();
        boolean[] dp = new boolean[n + 1]; // 빈 문자열을 대비해서 +1 길이로 설정
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

    public boolean wordBreak2(String s, List<String> wordDict) {
        int n = s.length();
        // List를 HashSet 객체 생성시 인자로 넣어 초기화가 가능합니다.
        // set은 List에서의 단어 탐색을 O(1) 성능으로 최적화하기 위해서 필요합니다.
        Set<String> wordSet = new HashSet<>(wordDict);

        // 빈 문자열일 경우를 대비해서 +1을 길이로 설정합니다.
        boolean[] dp = new boolean[n + 1];
        // 빈 문자열을 항상 true이므로 0번째 dp[]에 true를 설정합니다.
        dp[0] = true;

        // 앞서 빈문자열을 셋팅했으니 i는 1부터 n까지 반복합니다.
        // j는 0부터 i보다 작을때까지 반복합니다.
        /**
         * j=0: s.substring(0, 1) = "l" | dp[0]=true | "l" in dict=false
         * -----
         * j=0: s.substring(0, 2) = "le" | dp[0]=true | "le" in dict=false
         * j=1: s.substring(1, 2) = "e"  | dp[1]=false | "e" in dict=false
         * -----
         * j=0: s.substring(0, 3) = "lee" | dp[0]=true | "lee" in dict=false
         * j=1: s.substring(1, 3) = "ee"  | dp[1]=false | "ee" in dict=false
         * j=2: s.substring(2, 3) = "e"   | dp[2]=false | "e" in dict=false
         * -----
         * j=0: s.substring(0, 4) = "leet" | dp[0]=true | "leet" in dict=true → dp[4] = true!
         * -----
         * j=0: s.substring(0, 5) = "leetc" | dp[0]=true | "leetc" in dict=false
         * j=1: s.substring(1, 5) = "eetc"  | dp[1]=false | "eetc" in dict=false
         * j=2: s.substring(2, 5) = "etc"   | dp[2]=false | "etc" in dict=false
         * j=3: s.substring(3, 5) = "tc"    | dp[3]=false | "tc" in dict=false
         * j=4: s.substring(4, 5) = "c"     | dp[4]=true | "c" in dict=false
         * -----
         * j=0: s.substring(0, 8) = "leetcode" | dp[0]=true | "leetcode" in dict=false
         * j=1: s.substring(1, 8) = "eetcode"  | dp[1]=false | "eetcode" in dict=false
         * j=2: s.substring(2, 8) = "etcode"   | dp[2]=false | "etcode" in dict=false
         * j=3: s.substring(3, 8) = "tcode"    | dp[3]=false | "tcode" in dict=false
         * j=4: s.substring(4, 8) = "code"     | dp[4]=true | "code" in dict=true → dp[8] = true!
         */
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j < i; j++) {
                // 예시를 보면 (start, end)에서 start가 증가할 동안 end는 고정됩니다. 따라서 start=j, end=i가 되어야 합니다.
                if (dp[j] && wordSet.contains(s.substring(j, i))) {
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[n];
    }
}
