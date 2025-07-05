/**
 * 문제 설명
 * - 0부터 n까지의 모든 수에 대해 이진수에서 1의 개수를 세는 함수를 작성하라.
 *
 * 아이디어
 * 1) DP + 비트연산
 *   - ans[i] = ans[i >> 1] + (i & 1)
 */
function countBits(n: number): number[] {
  const ans = Array(n + 1).fill(0);
  for (let i = 1; i <= n; i++) {
    ans[i] = ans[i >> 1] + (i & 1);
  }
  return ans;
}
