/**
 * [Idea] - Dynamic programming
 * 현재 계단에 도달하기 위해서는 1칸 전 계단에서 1칸 올라오거나 2칸 전 계단에서 2칸 올라와야 한다.
 * memo[i] = memo[i - 1] + memo[i - 2] 로 계산할 수 있다.
 *
 * [Time Complexity]
 * O(n) (n: 계단의 개수)
 * 계단의 개수만큼 반복문을 돈다.
 *
 * [Space Complexity]
 * O(n) (n: 계단의 개수)
 * memo 배열을 n + 1 크기로 생성한다.
 */
function climbStairs(n: number): number {
  const memo = new Array<number>(n + 1).fill(0);
  memo[1] = 1;
  memo[2] = 2;

  for (let currStep = 3; currStep <= n; currStep++) {
    memo[currStep] = memo[currStep - 1] + memo[currStep - 2];
  }

  return memo[n];
}
