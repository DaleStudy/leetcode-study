// O(N^2) 이 나올 수밖에 없는 문제. 이런 문제의 특징은 N의 크기가 작다.
// 이번문제도 N의 크기가 1000으로 주어졌을때, 이차원 for문이 허용된다는걸 간접적으로 알아챌 수 있다.
// 이차원 배열 이므로 공간복잡도도 O(N^2)
class Solution {
    public int countSubstrings(String s) {
        int n = s.length();
        boolean[][] dp = new boolean[n][n];
        int count = 0;

        for (int i = 0; i < n; i++) {
            dp[i][i] = true;
            count++;
        }

        for (int len = 2; len <= n; len++) {
            for (int i = 0; i <= n - len; i++) { // 시작 위치
                int j = i + len - 1; // 끝 위치

                // 양 끝 문자가 같고, 내부가 회문이거나 길이가 2인 경우
                if (s.charAt(i) == s.charAt(j)) {
                    if (len == 2 || dp[i + 1][j - 1]) {
                        dp[i][j] = true;
                        count++;
                    }
                }
            }
        }

        return count;
    }
}