function combinationSum(candidates: number[], target: number): number[][] {
  const results: number[][] = [];

  function backtrack(currentIndex: number, sum: number, selected: number[]) {
    if (sum > target) return;
    if (sum === target) {
      results.push([...selected]);
      return;
    }

    for (let i = currentIndex; i < candidates.length; i++) {
      selected.push(candidates[i]);
      backtrack(i, sum + candidates[i], selected);
      selected.pop();
    }
  }

  backtrack(0, 0, []);

  return results;
}
