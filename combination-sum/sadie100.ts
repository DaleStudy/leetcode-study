/*
dfs로 각 candidates를 돌면서 target과 같아지는 순간에 result를 반환한다.

같은 조합이 중복됨을 피하기 위해 candidates를 정렬하고, 각 숫자보다 크거나 같은 candidate만 탐색한다.

시간복잡도 : O(N^(T/min(c))) - N은 candidates의 수, T는 타겟, c는 candidates.
타겟을 candidates의 최소값으로 나눈 값이 최대 깊이이므로 최악의 경우 해당 횟수만큼 반복해서 배열을 탐색함
*/

function combinationSum(candidates: number[], target: number): number[][] {
  candidates.sort((a, b) => a - b)
  const result = []
  const search = (idx, nums, sum) => {
    if (sum === target) {
      result.push(nums)
      return
    }
    for (let i = idx; i < candidates.length; i++) {
      const num = candidates[i]
      if (sum + num > target) return
      search(i, [...nums, num], sum + num)
    }
  }

  search(0, [], 0)

  return result
}
