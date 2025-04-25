/**
 주어진 문자열을 복호화 할 수 있는 경우의 수를 반환하시오.
 문자열은 A-Z까지 숫자 1-26으로 치환
 예시: "AAJF" => (1, 1, 10, 6), (11, 10, 6)...
 */
class Solution {

    // 시간복잡도: O(n), 공간복잡도: O(n)
    public int numDecodings(String s) {

        int[] dp = new int[s.length() + 1];

        // contain leading zero(s)
        if (s.charAt(0) == '0') {
            return 0;
        }

        dp[0] = 1;
        dp[1] = 1;

        for (int i = 2; i <= s.length(); i++) {

            // 1자리수 검사
            int one = Integer.parseInt(Character.toString(s.charAt(i - 1)));

            if (one != 0) {
                dp[i] += dp[i - 1];
            }

            // 2자리수 검사
            int two = Integer.parseInt(Character.toString(s.charAt(i - 2))) * 10 + one;

            if (two >= 10 && two <= 26) {
                dp[i] += dp[i - 2];
            }

        }

        return dp[s.length()];
    }

}

