/*

n+1개의 배열을 만들고 순회를 돌리며 i-1, i-2를 합한다

시간복잡도 : O(N) => n 배열 순회
공간복잡도 : O(N) => n+1 배열
*/

function climbStairs(n: number): number {
  const stair = new Array(n + 1).fill(0)

  stair[0] = 1
  stair[1] = 1

  if (n < 1) return stair[n]

  for (let i = 2; i < n + 1; i++) {
    stair[i] = stair[i - 1] + stair[i - 2]
  }

  return stair[n]
}
