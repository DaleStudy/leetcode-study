function combinationSum(candidates: number[], target: number): number[][] {
  const result: number[][] = [];

  function backtracking(start: number, current: number[], remaining: number) {
      if(remaining < 0) return;
      if(remaining === 0) {
          result.push([...current]);
          return;
      }

      for(let i = start; i < candidates.length; i++) {
          current.push(candidates[i]);
          backtracking(i, current, remaining - candidates[i]);
          current.pop();
      }
  }
  backtracking(0, [], target)
  return result;
};
