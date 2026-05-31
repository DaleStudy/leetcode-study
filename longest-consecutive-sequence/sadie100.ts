/**
nums를 Set으로 만들어서 중복을 제거하고 순회하면서 시작점(n-1이 Set에 없는 수)을 찾아 연속된 수를 찾아가며 length를 계산한다.
시작점이 아닌 num(set에 num-1이 있는 경우)는 순회하지 않는다.

시간복잡도
O(N) : 이중 반복문이지만 시작점에서만 탐색하므로 깊은 중복 순회가 없음
 */

function longestConsecutive(nums: number[]): number {
  if (nums.length === 0) return 0
  const numSet = new Set(nums)
  let result = 1

  for (let num of numSet) {
    if (numSet.has(num - 1)) {
      continue
    }

    let next = num + 1
    let count = 1
    while (numSet.has(next)) {
      count += 1
      next += 1
    }

    result = Math.max(result, count)
  }

  return result
}
