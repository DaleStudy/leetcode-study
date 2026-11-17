/* 
시간 복잡도(TC): O(n)
공간 복잡도(SC): O(1)
풀이: Dynamic Programming을 활용하여 작은 문제 단위로 쪼갠다. Memoisation 혹은 Tabluation을 통해 시간 복잡도를 크게 단축시키는 것이 관건.
기타: Dynamic Programming은 이론과 달리 실제 문제에 적용하는 것이 익숙하지 않은 상황. 따라서 추후 보충 학습이 필요함. 🟡자력 해결 실패. 

풀이 이력
1트: Dynamic Programming을 활용했으나, Memoisation & Tabluation을 적용하지 않아 시간 복잡도가 O(2^n). TLE 발생.
2트: Memoisation 적용 
3트: Tabulation 적용
4트: Tabulation & Space-Optimisation

원리
i < 0: 계단을 내려간 경우, 0을 반환한다. (불가능)
i = 0: 계단을 다 내려간 경우, 1을 반환한다. (가능)
본 문제에서 1 <= n <= 45을 제시했으므로, n < 0은 고려하지 않고 i <= 1일 때의 경우만 고려한다.

점화식: dp[i] = dp[i-1] + dp[i-2]
n = 2부터 for iteration을 전개하여 dp[i]를 계산한다. dp[i]는 i번째 계단에 도달하는 방법의 수를 의미한다.
Space-Optimisation: dp[i]를 계산할 때, dp[i-1]과 dp[i-2]만 필요하므로, dp 배열을 선언하지 않고 prev1, prev2 변수를 활용하여 공간 복잡도를 O(1)로 줄인다.
*/

const climbStairs = (n: number): number => {
  if (n <= 1) return 1
  let prev2 = 1
  let prev1 = 1

  for (let i = 2; i <= n; i++) {
    const current = prev1 + prev2

    prev2 = prev1
    prev1 = current
  }

  return prev1
}

/* 풀이 이력(History) */
/* 1트: Only Dynamic Programming(NG)

const factrorialClimbStairs = (n: number): number => {
    if(n < 0) return 0
    if(n === 0) return 1

    return climbStairs(n - 1) + climbStairs(n - 2)
} 

*/

/* 2트: Memoisation 활용(Top-down DP)

const countRecur = (n: number, memo: number[]) => {
    // Base case
    if (n < 0)
        return 0

    if (n === 0)
        return 1

    // If value is memoised
    if (memo[n] !== -1) {
        return memo[n]
    }

    // Memoise the state (dp[n] = dp[n-1] + dp[n-2])
    memo[n] = countRecur(n - 1, memo) + 
              countRecur(n - 2, memo)

    return memo[n]
}

const memoisedClimbStairs = (n: number) => {
    const memo = Array(n + 1).fill(-1)
    return countRecur(n, memo)
}
*/

/* 3트: Tabulation(Bottom-up) -> 시간 복잡도는 충족. 하지만 공간 복잡도 역시 개선 가능한 상황.
const tabulatedClimbStairs = (n: number): number => {
    const dp = new Array(n + 1).fill(0)
    dp[0] = 1 // n = 0일 때에는 1로 고정이 된다. 아래 for itearion은 n = 1부터 시작하므로 dp[0]을 초기화해주어야 한다.

    for(let i = 1; i <= n; i++) {
        dp[i] = 0

        // 점화식: dp[i] = dp[i-1] + dp[i-2]에 의해 Tabulation 작업을 수행함.
        if (i - 1 >= 0) dp[i] += dp[i - 1]
        if (i - 2 >= 0) dp[i] += dp[i - 2]
    }

    return dp[n]
} 

*/
