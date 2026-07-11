/**
 * 시간 복잡도: O(n^target)
 * 공간 복잡도: O(target)
 */
function combinationSum(candidates: number[], target: number): number[][] {
  const result: number[][] = [];
  const current: number[] = [];

  function backtracking(index: number, remain: number) {
    if (remain === 0) {
      result.push([...current]);
      return;
    }

    if (remain < 0) {
      return;
    }

    for (let i = index; i < candidates.length; i++) {
      current.push(candidates[i]);
      backtracking(i, remain - candidates[i]);
      current.pop();
    }
  }

  backtracking(0, target);
  return result;
}
