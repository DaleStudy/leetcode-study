/**
 * @description 1칸 또는 2칸씩 올라갈 수 있을 때 n번째 계단에 도달하는 경우의 수
 * 점화식: ways(n) = ways(n-1) + ways(n-2)
 * @param {number} n - 계단의 총 개수
 * @returns {number} n번째 계단까지 올라가는 서로 다른 방법의 수
 */
function climbStairs(n: number): number {
  // base case
  // n이 1이면 1가지
  // n이 2이면 (1+1, 2) 총 2가지
  if (n <= 2) return n;

  // a = ways(n-2)
  // b = ways(n-1)
  let a = 1;
  let b = 2;

  // 3번째 계단부터 n번째 계단까지 경우의 수를 계산
  for (let i = 3; i <= n; i++) {
    // 현재 계단(i)에 도달하는 경우의 수
    // = 바로 전 계단(i-1) + 두 칸 전 계단(i-2)
    const c = a + b;

    // 다음 계산을 위해 값 이동
    // a ← 이전 ways(i-1)
    // b ← 현재 ways(i)
    a = b;
    b = c;
  }

  return b;
}
