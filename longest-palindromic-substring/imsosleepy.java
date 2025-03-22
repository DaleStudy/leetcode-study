// 투포인터와 유사한 방식의 풀이가 하나 더 있었음
// 다만 모든 문자열이 가운데가 될 수 있다는 조건이 너무 까다로워서 구현에는 실패함
// DP와 같은 O(N^2)이 되지만 공간사용량이 압도적으로 적어서 시간차이가 많이 나게 됨
// GPT의 도움을 받았음
class Solution {
    public String longestPalindrome(String s) {
        if (s == null || s.length() < 1) return "";
        
        int start = 0, end = 0;
        
        for (int i = 0; i < s.length(); i++) {
            int len1 = expandAroundCenter(s, i, i);
            int len2 = expandAroundCenter(s, i, i + 1);
            int len = Math.max(len1, len2);
            

            if (len > end - start) {
                start = i - (len - 1) / 2;
                end = i + len / 2;
            }
        }
        
        return s.substring(start, end + 1);
    }
    
    private int expandAroundCenter(String s, int left, int right) {
        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
        }
        return right - left - 1;
    }
}

// 가장 먼저 생각한 풀이. 회문하면 떠오르는게 DP인데 이런 방식을 바라는게 아닌거같음
class Solution {
    public String longestPalindrome(String s) {
        int n = s.length();
        boolean[][] dp = new boolean[n][n];
        
        int start = 0, maxLen = 1;

        // 길이가 1인 경우
        for (int i = 0; i < n; i++) {
            dp[i][i] = true;
        }

        // 길이가 2인 경우
        for (int i = 0; i < n - 1; i++) {
            if (s.charAt(i) == s.charAt(i + 1)) {
                dp[i][i + 1] = true;
                start = i;
                maxLen = 2;
            }
        }

        for (int len = 3; len <= n; len++) {
            for (int i = 0; i <= n - len; i++) {
                int j = i + len - 1;
                
                if (s.charAt(i) == s.charAt(j) && dp[i + 1][j - 1]) {
                    dp[i][j] = true;
                    start = i;
                    maxLen = len;
                }
            }
        }

        return s.substring(start, start + maxLen);
    }
}
