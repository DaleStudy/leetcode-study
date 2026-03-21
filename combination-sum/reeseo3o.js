const combinationSum = (candidates, target) => {
  const result = [];

  const backtrack = (startIndex, current, remaining) => {
    if (remaining === 0) {
      result.push([...current]);
      return;
    }
    if (remaining < 0) return;

    for (let i = startIndex; i < candidates.length; i++) {
      current.push(candidates[i]);
      backtrack(i, current, remaining - candidates[i]);
      current.pop();
    }
  };

  backtrack(0, [], target);
  return result;
};
