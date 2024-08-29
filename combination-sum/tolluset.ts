/**
 * TC: O(candidates.length ^ target / min(candidates))
 * SC: O(target / min(candidates)
 */
function combinationSum(candidates: number[], target: number): number[][] {
  const result: number[][] = [];
  const dfs = (start: number, stop: number, path: number[]) => {
    if (stop === 0) {
      result.push([...path]);
      return;
    }

    for (let i = start; i < candidates.length; i++) {
      if (candidates[i] <= stop) {
        path.push(candidates[i]);
        dfs(i, stop - candidates[i], path);
        path.pop();
      }
    }
  };
  dfs(0, target, []);

  return result;
}
