/**
 * 풀이 1
 * - 2차원 DP를 사용하여 풀이합니다
 *   DP[i][j]: text1의 i번째 문자까지와 text2의 j번째 문자까지 비교했을 때, 가장 긴 공통 부분 문자열의 길이
 *             즉, text1[0 .. i - 1]와 text2[0 .. j - 1]의 가장 긴 공통 부분 문자열의 길이
 *   DP[i][j] = if text1[i - 1] == text2[j - 1] then DP[i - 1][j - 1] + 1
 *              else max(DP[i - 1][j], DP[i][j - 1])
 * - 풀이 2로 공간복잡도를 줄일 수 있습니다
 * 
 * Big O
 * - M: text1의 길이
 * - N: text2의 길이
 * 
 * - Time complexity: O(N * M)
 * - Space complexity: O(N * M)
 */

class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        size_t m = text1.size();
        size_t n = text2.size();

        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));

        for (int i = 1; i <= m; ++i) {
            for (int j = 1; j <= n; ++j) {
                if (text1[i - 1] == text2[j - 1]) dp[i][j] = dp[i - 1][j - 1] + 1;
                else dp[i][j] = max(dp[i][j - 1], dp[i - 1][j]);
            }
        }

        return dp[m][n];
    }
};

/**
 * 풀이 2
 * - 풀이 1의 DP 전개 과정을 보면 우리한테는 DP 배열 두 행만 필요하다는 걸 알 수 있습니다
 * 
 * Big O
 * - M: text1의 길이
 * - N: text2의 길이
 * 
 * - M >= N이 되도록 고릅니다
 * 
 * - Time complexity: O(N * M)
 * - Space complexity: O(N)
 */

class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        size_t m = text1.size();
        size_t n = text2.size();

        if (m < n) return longestCommonSubsequence(text2, text1);

        vector<int> dp1(n + 1, 0);
        vector<int> dp2(n + 1, 0);

        for (int i = 1; i <= m; ++i) {
            for (int j = 1; j <= n; ++j) {
                if (text1[i - 1] == text2[j - 1]) dp2[j] = dp1[j - 1] + 1;
                else dp2[j] = max(dp1[j], dp2[j - 1]);
            }

            if (i == m) break;

            dp1.swap(dp2);
            dp2.clear();
            dp2.resize(n + 1, 0);
        }

        return dp2[n];
    }
};
