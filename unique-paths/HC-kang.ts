/**
 * Solution 1. recursive - failed with Stack Overflow
 */
function uniquePaths(m: number, n: number): number {
  function factorialMemo() {
    const cache = [0, 1];
    return function factorial(n: number) {
      if (cache[n]) return cache[n];
      cache[n] = n * factorial(n - 1);
      return cache[n];
    };
  }

  const factorial = factorialMemo();
  const total = m + n - 2;
  const right = m - 1;
  return Math.round(
    factorial(total) / (factorial(right) * factorial(total - right))
  );
}

/**
 * Solution 2. for loop (with some 야매.. but it works)
 * https://leetcode.com/problems/unique-paths
 * T.C. O(m + n)
 * S.C. O(m + n)
 */
function uniquePaths(m: number, n: number): number {
  function factorialMemo() {
    const cache = [1, 1];
    return function factorial(n: number) {
      if (cache[n]) return cache[n];
      let result = cache[cache.length - 1];
      for (let i = cache.length; i <= n; i++) {
        result = result * i;
        cache[i] = result;
      }
      return result;
    };
  }

  const factorial = factorialMemo();
  const total = m + n - 2;
  const right = m - 1;
  return Math.round(
    factorial(total) / (factorial(right) * factorial(total - right))
  );
}

/**
 * Solution 3. DP
 * T.C. O(m * n)
 * S.C. O(m * n)
 */
function uniquePaths(m: number, n: number): number {
  const dp: number[][] = Array.from({ length: m }, () => Array(n).fill(1));

  for (let i = 1; i < m; i++) {
    for (let j = 1; j < n; j++) {
      dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
    }
  }

  return dp[m - 1][n - 1];
}
