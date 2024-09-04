// T.C: O(n^t) // n: candidates.length, t: target
// S.C: O(n)
function combinationSum(candidates: number[], target: number): number[][] {
  const result: number[][] = [];
  function dfs(start: number, target: number, path: number[]) {
    if (target < 0) return;
    if (target === 0) {
      result.push([...path]);
      return;
    }
    for (let i = start; i < candidates.length; i++) {
      path.push(candidates[i]);
      dfs(i, target - candidates[i], path);
      path.pop();
    }
  }
  dfs(0, target, []);
  return result;  
};
