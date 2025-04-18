function combinationSum(candidates: number[], target: number): number[][] {
  const result: number[][] = [];

  const dfs = (start: number, target: number, path: number[]) => {
      if (target === 0) {
          result.push([...path]);
          return;
      }

      for (let i = start; i < candidates.length; i++) {
          if (candidates[i] > target) continue;

          path.push(candidates[i]);
          dfs(i, target - candidates[i], path);
          path.pop();
      }
  }

  candidates.sort((a, b) => a - b);
  dfs(0, target, []);
  return result;
};