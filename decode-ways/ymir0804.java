class Solution {
    public int numDecodings(String s) {
        if (s == null || s.length() == 0 || s.charAt(0) == '0') {
            return 0;
        }

        int n = s.length();
        int[] dp = new int[n + 1];

        dp[0] = 1; // 빈 문자열을 해석하는 경우의 수는 1
        dp[1] = 1; // 첫 글자가 '0'이 아님을 위에서 체크했으므로 1 확정

        // 2. DP 수행 (Bottom-Up)
        for (int i = 2; i <= n; i++) {
            // 현재 문자와 바로 앞 문자 추출
            // DP 인덱스 i는 문자열의 i번째 글자(인덱스 i-1)를 의미함
            char current = s.charAt(i - 1);
            char prev = s.charAt(i - 2);

            // Case 1: 한 자리 숫자 해석 (1 ~ 9)
            // 현재 숫자가 '1'~'9'라면, 바로 직전 단계(i-1)의 경우의 수를 계승
            if (current >= '1' && current <= '9') {
                dp[i] += dp[i - 1];
            }

            // Case 2: 두 자리 숫자 해석 (10 ~ 26)
            // 이전 숫자와 합쳐서 값을 계산
            int twoDigit = (prev - '0') * 10 + (current - '0');

            if (twoDigit >= 10 && twoDigit <= 26) {
                dp[i] += dp[i - 2];
            }
        }

        // 3. 결과 반환
        return dp[n];
    }
}
