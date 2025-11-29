// 시간 복잡도: O(2^(target / minCandidate))
// 공간 복잡도: O(target / minCandidate)
function combinationSum(candidates: number[], target: number): number[][] {
  const result: number[][] = [];

  const dfs = (index: number, remain: number, path: number[]) => {
    if (remain === 0) {
      result.push([...path]);
      return;
    }

    if (remain < 0 || index === candidates.length) {
      return;
    }

    const num = candidates[index];

    path.push(num);
    dfs(index, remain - num, path);
    path.pop();

    dfs(index + 1, remain, path);
  };

  dfs(0, target, []);

  return result;
}
