/**
 * [풀이 개요]
 * - 시간복잡도 : O(n)
 * - 공간복잡도 : O(n)
 */
class Solution {
    /**
     * [문제 풀이 아이디어]
     * -  한 글자로 파싱이 되는 경우의 수와 두 글자로 파싱이 되는 경우 수를 합하면 될 것 같음
     * - 시간복잡도는 각 인덱스를 처음 한번 들린 이 후로는 dp 배열에서 O(1)에 리턴하므로 O(n).
     * - 공간복잡도는 문자열 길이 만큼의 dp 배열을 생성하므로 O(n)
     */
    public int numDecodings(String s) {
        int len = s.length();
        int[] dp = new int[len + 1];
        Arrays.fill(dp, -1);
        return count(0, s, len, dp);
    }

    /**
     * [시뮬레이션]
     * Case : 226
     * count(0, 226, {-1,-1,-1})
     *   += count(1, 226, {-1,-1,-1}) return 2 / 2
     *     += count(2, 226, {-1,-1,-1}) return 1 / 2 2
     *       += count(3, 226, {-1,-1,-1}) return 1 / 2 2 6
     *       += 0 (4 > limit)
     *     += count(3, 226, {-1,-1,-1}) return 1 / 2 26 / cashing
     *   += count(2, 226, {-1,-1,-1}) return 1 / 22 / cashing
     *     += count(3, 226, {-1,-1,-1}) return 1 / 22 6 / cashing
     * = 1 + 2 = 3
     */
    public int count(int start, String s, int limitIndex, int[] dp) {
        if(start == limitIndex) {
            return 1;
        }
        // 0으로 시작할 수 없음
        if(s.charAt(start) == '0') {
            return 0;
        }

        if(dp[start] != -1) {
            return dp[start];
        }

        int totalWays = 0;

        if(start + 1 <= limitIndex) {
            totalWays += count(start + 1, s, limitIndex, dp);
        }

        if(start + 2 <= limitIndex) {
            String numStr = s.substring(start, start+2);
            if(Integer.parseInt(numStr) <= 26) {
                totalWays += count(start + 2, s, limitIndex, dp);
            }
        }
        dp[start] = totalWays;
        return totalWays;
    }
}