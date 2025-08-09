class Solution {
    public int numDecodings(String s) {
        // 0 으로 시작하거나 빈 문자열이면 해독불가
        int sLen =  s.length();
        if (sLen == 0 || s.charAt(0) == '0') return 0;

        int[] dp =  new int[sLen+1];

        dp[0] = 1;
        dp[1] = 1;

        for (int i = 2; i <= sLen; i++) {

            int num = Integer.parseInt(s.substring(i-2, i));
            // 1자리 숫자로 해독 가능한 경우
            if (s.charAt(i-1) != '0') {
                dp[i] += dp[i-1];
            }
            // 2자리 숫자로 해독 가능한 경우
            if (num >= 10 && num <= 26) {
                dp[i] += dp[i-2];
            }
        }
        return dp[sLen];
    }
}
