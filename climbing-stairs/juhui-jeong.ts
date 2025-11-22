/*

시간 복잡도: O(n)
공간 복잡도: O(1)

해당 문제를 구할 때 바로 생각나지 않아 leet code의 코멘트들을 보며 힌트를 구했습니다.
*/
function climbStairs(n: number): number {
  if (n <= 2) return n;

  let a = 1;
  let b = 2;
  for (let i = 3; i <= n; i++) {
    let c = a + b;
    a = b;
    b = c;
  }
  return b;
}
