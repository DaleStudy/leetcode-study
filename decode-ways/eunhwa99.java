import java.util.Arrays;

/**
 * 문제 풀이
 * 예제) 11106
 * 가장 큰 수는 2자리 이므로 한 번에 갈 수 있는 칸은 1~2칸
 * 현재 칸이 0일 경우는 칸 이동 불가
 * 코드 범위는 1~26
 */

//시간 복잡도:  문자열의 각 인덱스를 한 번씩만 처리하므로 전체 O(n)
//공간 복잡도: dp 배열은 문자열의 길이에 비례하여 O(n) 공간을 차지

class Solution {

    int stringSize = 0;
    int[] dp;

    // DP 이용
    public int numDecodings(String s) {
        stringSize = s.length();
        dp = new int[stringSize + 1];
        Arrays.fill(dp, -1);
        return numDecodingHelper(s.toCharArray(), 0);
    }

    // dp -> O(N)
    private int numDecodingHelper(char[] s, int curIndex) {
        if (stringSize == curIndex) return 1;
        if (s[curIndex] == '0') return 0; // 현재 칸이 0 -> 전진 불가
        if (dp[curIndex] != -1) return dp[curIndex];

        dp[curIndex] = 0; // 현재 노드 방문 체크
        dp[curIndex] += numDecodingHelper(s, curIndex + 1); // 한 칸 전진

        if ((curIndex + 1 < stringSize) && checkRange(s[curIndex], s[curIndex + 1])) // 2자리 코드가 10~26 안에 들어간다면
            dp[curIndex] += numDecodingHelper(s, curIndex + 2); // 2칸 전진

        return dp[curIndex];
    }

    private boolean checkRange(char left, char right) {
        int leftNum = left - '0';
        int rightNum = right - '0'; // 숫자로 변환

        int num = leftNum * 10 + rightNum;
        return (num >= 10 && num <= 26);
    }
}

// 시간 복잡도: O(n) - 문자열 길이 n에 비례
// 공간 복잡도: O(n) - dp 배열 사용
class newSolution {
    public int numDecodings(String s) {
        int n = s.length();
        if (n == 0 || s.charAt(0) == '0') return 0;

        int[] dp = new int[n + 1];
        dp[0] = 1; // 빈 문자열은 한 가지 방법
        dp[1] = 1; // 첫 문자가 0이 아니면 한 가지 방법

        for (int i = 2; i <= n; i++) {
            char one = s.charAt(i - 1);     // 한 자리 숫자
            char twoPrev = s.charAt(i - 2); // 두 자리 숫자의 앞자리

            // 1칸 이동 가능 (0은 이동 불가)
            if (one != '0') {
                dp[i] += dp[i - 1];
            }

            // 2칸 이동 가능한지 확인 (10~26)
            int num = (twoPrev - '0') * 10 + (one - '0');
            if (num >= 10 && num <= 26) {
                dp[i] += dp[i - 2];
            }
        }

        return dp[n];
    }
}

