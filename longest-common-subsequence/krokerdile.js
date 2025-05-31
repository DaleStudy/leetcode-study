/**
 * @param {string} text1
 * @param {string} text2
 * @return {number}
 * 
 * 시간복잡도: O(m * n)
 *    - m = text1.length, n = text2.length
 *    - 2중 for문으로 dp 테이블 채우기
 *
 * 공간복잡도: O(m * n)
 *    - dp 배열에 m * n 만큼의 공간 사용
 *    - 최적화하려면 배열 2개로도 가능
 */
var longestCommonSubsequence = function(text1, text2) {
    let m = text1.length;
    let n = text2.length;

    // 2차원 dp 배열 초기화 (m+1) x (n+1)
    const dp = Array.from({ length: m + 1 }, () => Array(n + 1).fill(0));

    // dp[i][j] = text1[0..i-1], text2[0..j-1] 까지의 LCS 길이
    for (let i = 1; i <= m; i++) {
        for (let j = 1; j <= n; j++) {
            if (text1[i - 1] === text2[j - 1]) {
                // 문자가 같으면, 이전까지의 LCS + 1
                dp[i][j] = dp[i - 1][j - 1] + 1;
            } else {
                // 아니면, 이전 행/열 중 더 큰 값 선택
                dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }

    return dp[m][n]; // 마지막 cell이 정답
};

//실패한 dfs 코드
/**
 * @param {string} text1
 * @param {string} text2
 * @return {number}
 */
var longestCommonSubsequence = function(text1, text2) {
    function dfs(i, j) {
        // 종료 조건: 인덱스 범위를 벗어나면 0
        if (i === text1.length || j === text2.length) {
            return 0;
        }

        // 문자가 같으면, 다음 문자로 이동하며 길이 +1
        if (text1[i] === text2[j]) {
            return 1 + dfs(i + 1, j + 1);
        }

        // 문자가 다르면, 두 가지 갈래 중 최댓값을 선택
        return Math.max(
            dfs(i + 1, j),     // text1의 다음 문자로
            dfs(i, j + 1)      // text2의 다음 문자로
        );
    }

    return dfs(0, 0);
};
