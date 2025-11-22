/**
 * 1 or 2 스텝 가능
 * @param n - 꼭대기
 * @returns - 꼭대기 까지 도달할 수 있는 방법 수
 * @description
 * - 결국 패턴은 피보나치
 * - 시간 복잡도 O(n)
 * - 공간 복잡도 O(1)
 */

// function climbStairs(n: number): number {
//   if (n <= 2) {
//     return n;
//   }

//   const dp = Array.from({ length: n + 1 }, () => 0);
//   dp[1] = 1;
//   dp[2] = 2;

//   for (let i = 3; i <= n; i++) {
//     dp[i] = dp[i - 1] + dp[i - 2];
//   }
//   return dp[n];
// }

function climbStairs(n: number): number {
  if (n <= 2) {
    return n;
  }

  let prevTwo = 1;
  let prevOne = 2;

  for (let i = 2; i <= n; i++) {
    const current = prevTwo + prevOne;
    prevTwo = prevOne;
    prevOne = current;
  }

  return prevOne;
}

const n = 3;
climbStairs(n);

