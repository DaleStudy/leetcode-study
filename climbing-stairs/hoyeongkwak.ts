/*
시간복잡도 : O(n)
공간복잡도 : O(1)
*/
function climbStairs(n: number): number {
  if (n < 3) return n
  let prev = 1
  let curr = 2
  for (let i = 0; i < n - 2; i++) {
    const tempPrev = prev
    prev = curr
    curr = tempPrev + curr
  }
  return curr
}
