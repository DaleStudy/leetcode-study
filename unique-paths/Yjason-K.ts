
/**
 * m * n 그리드에서 좌측 상단에서 우측 하단까지 갈 수 있는 경로의 수
 * @param {number} m - 그리드의 행 길이 
 * @param {number} n - 그리드의 열 길이
 * @returns {number} 우측 하단까지 갈 수 있는 경우의 수
 * 
 * - 시간 복잡도: O(m * n)
 *   - m x n 크기의 배열을 초기화하고 순회
 * 
 * - 공간 복잡도: O(m * n)
 *   - m x n 크기의 배열을 사용
 */
function uniquePaths(m: number, n: number): number {
    // m x n 크기의 배열을 초기화
    const dp = Array.from({ length: m }, () => Array(n).fill(0));

    // 첫 번째 셀 (0, 0)은 1로 초기화 (경로 시작점)
    dp[0][0] = 1;

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (i === 0 && j === 0) continue; // 시작점은 이미 초기화됨

            // 위쪽과 왼쪽 값을 더해 현재 셀의 경로 수 계산
            dp[i][j] = (dp[i - 1]?.[j] || 0) + (dp[i]?.[j - 1] || 0);
        }
    }

    return dp[m - 1][n - 1];
}

