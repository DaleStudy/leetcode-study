function combinationSum(candidates: number[], target: number): number[][] {
  const result: number[][] = [];

  const dfs = (start: number, path: number[], sum: number) => {
    if (sum === target) {
      result.push([...path]);
      return;
    }

    if (sum > target) {
      return;
    }

    for (let i = start; i < candidates.length; i++) {
      path.push(candidates[i]);
      dfs(i, path, sum + candidates[i]);
      path.pop();
    }
  };

  dfs(0, [], 0);
  return result;
}
