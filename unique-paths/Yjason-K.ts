
/**
 * m * n 그리드에서 좌측 상단에서 우측 하단까지 갈 수 있는 경로의 수
 * @param {number} m - 그리드의 행 길이 
 * @param {number} n - 그리드의 열 길이
 * @returns {number} 우측 하단까지 갈 수 있는 경우의 수
 * 
 * - 시간 복잡도: O(m * n)
 *   - 전체 셀을 한 번씩 순회
 * 
 * - 공간 복잡도: O(n)
 *   - 1차원 배열 사용 (열 크기만큼의 배열)
 */
function uniquePaths(m: number, n: number): number {
    // n(열) 크기의 배열을 생성
    const dp = Array(n).fill(1);


    for (let i = 1; i < m; i++) {
        for (let j = 1; j < n; j++) {
            // 현재 값 = 위쪽(dp[j]) + 왼쪽(dp[j-1])
            dp[j] = dp[j] + dp[j - 1];
        }
    }

     // dp[n-1]에 우측 하단까지의 경로 수가 저장
    return dp[n - 1];
}

