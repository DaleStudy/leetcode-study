/**
 * @description
 * 동적 프로그래밍(Dynamic Programming, DP)을 사용하여 계단을 오르는 방법 수를 계산합니다.
 * - 점화식: dp[i] = dp[i-1] + dp[i-2]
 * - dp[i-1]: 이전 계단에서 1단계 올라온 경우
 * - dp[i-2]: 두 계단 아래에서 2단계 올라온 경우
 * - 공간 최적화를 통해 배열 대신 두 변수(prev1, prev2)를 사용하여 메모리 사용량을 줄입니다.
 * @param {number}n step 수
 * @returns {number} 계단 도달 방법 수
 */
function climbStairs(n: number): number {
    if (n <=2) return n;

    let prev2 = 1; // dp[i-2]
    let prev1 = 2; // dp[i-1]  

    for (let i = 3; i <= n; i++) {
        const cur = prev1 + prev2; // dp[i] 계산
        prev2 = prev1; // dp[i-2] 갱신
        prev1 = cur;   // dp[i-1] 갱신
      }

    return prev1; // dp[n] 반환
};

