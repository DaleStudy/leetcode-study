function combinationSum(candidates: number[], target: number): number[][] {
  const results: number[][] = [];

  function comb(index: number, arr: number[], sum: number) {
    if (sum === target) {
      results.push([...arr]);
      return;
    }
    if (sum > target || candidates.length <= index) {
      return;
    }
    arr.push(candidates[index]);
    comb(index, arr, sum + candidates[index]);
    arr.pop();
    comb(index + 1, arr, sum);
  }

  comb(0, [], 0);
  return results;
}
