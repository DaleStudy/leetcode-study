/* 
시간 복잡도(TC): O(n)
공간 복잡도(SC): O(1)
풀이: Dynamic Programming을 활용하여 작은 문제 단위로 쪼갠다. Memoisation 혹은 Tabluation을 통해 시간 복잡도를 크게 단축시키는 것이 관건.

풀이 이력
1트: Dynamic Programming을 활용했으나, Memoisation & Tabluation을 적용하지 않아 시간 복잡도가 O(2^n). TLE 발생.
2트: Memoisation 적용 
3트: Tabulation 적용
4트: Tabulation & Space-Optimisation
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

const climbStairs = (n: number): number => {
    if(n < 0) return 0
    if(n === 0) return 1

    return climbStairs(n - 1) + climbStairs(n - 2)
} 

*/

/* 2트: Memoisation 활용(Top-down DP)

const countRecur = (n: number, memo: number[]) => {
    if (n < 0)
        return 0

    if (n === 0)
        return 1

    // If value is memoised
    if (memo[n] !== -1) {
        return memo[n]
    }

    // Memoize the state 
    memo[n] = countRecur(n - 1, memo) + 
              countRecur(n - 2, memo)

    return memo[n]
}

const climbStairs = (n: number) => {
    const memo = Array(n + 1).fill(-1)
    return countRecur(n, memo)
}
*/

/* 3트: Tabulation(Bottom-up) -> 시간 복잡도는 충족. 하지만 공간 복잡도 역시 개선 가능한 상황.
const climbStairs = (n: number): number => {
    const dp = new Array(n + 1).fill(0)
    dp[0] = 1

    for(let i = 1; i <= n; i++) {
        dp[i] = 0

        if (i - 1 >= 0) dp[i] += dp[i - 1]
        if (i - 2 >= 0) dp[i] += dp[i - 2]
    }

    return dp[n]
} 

*/
