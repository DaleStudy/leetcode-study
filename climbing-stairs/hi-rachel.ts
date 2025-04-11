// n steps의 계단 오르기
// 한 번에 1 혹은 2 steps 오르기 가능
// 오를 수 있는 방법의 수 반환해라
// O(n) time, O(n) space

function climbStairs(n: number): number {
  let ways: number[] = [];
  ways[0] = 1;
  ways[1] = 2;

  for (let i = 2; i < n; i++) {
    ways[i] = ways[i - 1] + ways[i - 2];
  }
  return ways[n - 1];
}
