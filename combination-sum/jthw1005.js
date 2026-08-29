function combinationSum(candidates, target) {
  const dp = Array.from({ length: target + 1 }, () => []);
  dp[0] = [[]];
  for (let i = 0; i < candidates.length; i++) {
    for (let j = candidates[i]; j <= target; j++) {
      dp[j].push(
        ...dp[j - candidates[i]].map((item) => [...item, candidates[i]]),
      );
    }
  }
  return dp[target];
}
