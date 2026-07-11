/**
 * 시간 복잡도: O(k * n^k) (n: candidates 길이, k: target / min(candidates) 최대 깊이)
 * 공간 복잡도: O(k)
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
