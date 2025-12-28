/**
 * Unique Paths - 조합론 방식
 *
 * 문제: m x n 그리드에서 (0,0)에서 (m-1, n-1)까지 가는 경로의 수
 * - 오른쪽 또는 아래로만 이동 가능
 *
 * 핵심 아이디어:
 * - 총 이동 횟수: (m-1) + (n-1) = m+n-2번
 * - 오른쪽 n-1번, 아래 m-1번 이동 필요
 * - 순서만 다른 조합 문제: C(m+n-2, m-1) 또는 C(m+n-2, n-1)
 *
 * 예: m=3, n=7
 * - 총 8번 이동 (오른쪽 6번, 아래 2번)
 * - C(8, 2) = 8!/(2!*6!) = 28
 *
 * 시간복잡도: O(min(m, n)) - 조합 계산
 * 공간복잡도: O(1)
 *
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var uniquePaths = function(m, n) {
    // C(m+n-2, m-1) = (m+n-2)! / ((m-1)! * (n-1)!)
    // = (m+n-2) * (m+n-3) * ... * n / (m-1)!

    let total = m + n - 2;  // 총 이동 횟수
    let k = Math.min(m - 1, n - 1);  // 작은 쪽 선택 (계산 효율)

    let result = 1;

    // C(total, k) 계산
    for (let i = 1; i <= k; i++) {
        result = result * (total - k + i) / i;
    }

    return result;
};

// 테스트
if (require.main === module) {
    console.log(uniquePaths(3, 7));  // 28
    console.log(uniquePaths(3, 2));  // 3
    console.log(uniquePaths(1, 1));  // 1
}
