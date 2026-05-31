function combinationSum(candidates: number[], target: number): number[][] {
  const answer: number[][] = [];

  function dfs(index: number, path: number[], sum: number) {
    if (sum === target) {
      answer.push([...path]);
      return;
    }
    if (sum > target) return;

    for (let i = index; i < candidates.length; i++) {
      path.push(candidates[i]);            
      dfs(i, path, sum + candidates[i]);   
      path.pop();                          
    }
  }

  dfs(0, [], 0);
  return answer;
}
