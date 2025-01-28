/**
 * 두 문자열의 최장 공통 부분 문자열의 길이 구하기.
 * 
 * @param {string} text1 - 첫 번째 문자열
 * @param {string} text2 - 두 번째 문자열
 * @returns {number} - 최장 공통 부분 문자열의 길이
 * 
 * 시간 복잡도:
 * - O(m * n) : 두 문자열의 길이를 각각 m, n이라고 할 때, DP 테이블의 모든 요소를 계산합니다.
 * 
 * 공간 복잡도:
 * - O(m * n) : m+1 x n+1 크기의 2차원 DP 테이블을 생성하여 사용합니다.
 */
function longestCommonSubsequence(text1: string, text2: string): number {
    const m = text1.length;
    const n = text2.length;

    // DP 테이블 생성 (m+1 x n+1 크기)
    const dp: number[][] = Array.from({ length: m + 1 }, () => Array(n + 1).fill(0));

    // DP 계산
    for (let i = 1; i <= m; i++) {
        for (let j = 1; j <= n; j++) {
            if (text1[i - 1] === text2[j - 1]) {
                // 문자가 일치하면 이전 값에 +1
                dp[i][j] = dp[i - 1][j - 1] + 1;
            } else {
                // 문자가 다르면 왼쪽과 위쪽 값 중 큰 값 선택
                dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }

    // 최장 공통 부분 문자열의 길이
    return dp[m][n];
}

