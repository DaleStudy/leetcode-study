// [39] Combination Sum

function combinationSum(candidates: number[], target: number): number[][] {
  const n = candidates.length;
  const output: number[][] = [];

  function dfs(arr: number[], startIdx: number, sum: number) {
    if (sum === target) {
      output.push([...arr]);
      return;
    }
    if (sum > target) return;

    // 현재 숫자부터 다시 시작 (중복 선택이 가능하기 때문)
    for (let idx = startIdx; idx < n; idx++) {
      arr.push(candidates[idx]);
      dfs(arr, idx, sum + candidates[idx]);
      arr.pop();
    }
  }

  dfs([], 0, 0);

  return output;
}
