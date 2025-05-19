function combinationSum(candidates: number[], target: number): number[][] {
  const dp: number[][][] = Array(target + 1).fill(null).map(() => [])
  dp[0] = [[]]

  for (let i = 1; i <= target; i++){
    for (const num of candidates) {
        if (i - num >= 0 && dp[i - num].length > 0) {
            for (const combo of dp[i - num]) {
                if (combo.length === 0 || num >= combo[combo.length - 1]) {
                    dp[i].push([...combo, num])
                }
            }
        }
    }
  }
  return dp[target]
};
