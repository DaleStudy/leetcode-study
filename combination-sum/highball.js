const combinationSum = function (candidates, target) {
  const result = [];
  const path = [];

  const dfs = function (candidate, sum) {
    if (sum > target) return;

    if (sum !== 0) path.push(candidate);

    if (sum === target) {
      result.push([...path]);
      path.pop();
      return;
    }

    for (let i = 0; i < candidates.length; i++) {
      if (candidates[i] >= candidate) dfs(candidates[i], sum + candidates[i]);
    }

    path.pop();
  };

  dfs(0, 0);

  return result;
};

console.log(combinationSum([2, 3, 5], 8));
