/**
 * 가장 긴 공통 부분 수열의 길이를 반환하는 함수
 * @param {string} text1
 * @param {string} text2
 * @return {number}
 */
const longestCommonSubsequence = function (text1, text2) {
    const dp = Array.from({ length: text1.length }, () => Array.from({ length: text2.length }, () => -1));

    // text1, 2를 순회하는 포인터 i, j를 두고, 두 문자끼리 비교하는 함수
    function dfs(i, j) {
        // 포인터가 범위를 넘어가면 백트래킹
        if (i === text1.length || j === text2.length) {
            return 0;
        }

        // 두 문자를 이미 비교한 적 있는 경우 해당 결과 반환
        if (dp[i][j] !== -1) {
            return dp[i][j];
        }

        // 두 문자를 비교
        if (text1[i] === text2[j]) {
            dp[i][j] = 1 + dfs(i + 1, j + 1);
        } else {
            dp[i][j] = Math.max(dfs(i + 1, j), dfs(i, j + 1));
        }

        return dp[i][j];
    }

    return dfs(0, 0);
};

// 시간복잡도: O(m * n) (m: text1.length, n: text2.length)
// 공간복잡도: O(m * n) (재귀 호출 깊이: m + n, dp 배열 크기: m * n)
