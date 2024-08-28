/**
 * TC: O(candidates.length ^ target / min(candidates))
 * SC: O(target / min(candidates)
 */
function combinationSum(candidates: number[], target: number): number[][] {
  const result: number[][] = [];
  const dfs = (start: number, spot: number, path: number[]) => {
    if (spot === 0) {
      result.push([...path]);
      return;
    }

    for (let i = start; i < candidates.length; i++) {
      if (candidates[i] <= spot) {
        path.push(candidates[i]);
        dfs(i, spot - candidates[i], path);
        path.pop();
      }
    }
  };
  dfs(0, target, []);

  return result;
}
