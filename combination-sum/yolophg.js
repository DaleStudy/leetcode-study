// Time Complexity: O(n * target * k)
// Space Complexity: O(target)

var combinationSum = function (candidates, target) {
  // initialize dp array to store combinations
  const dp = Array(target + 1)
    .fill(null)
    .map(() => []);

  // sort candidates to ensure uniqueness and optimize processing
  candidates.sort((a, b) => a - b);

  // one way to make sum 0 (by choosing no elements)
  dp[0] = [[]];

  // iterate through each candidate
  for (let num of candidates) {
    // update dp array for current candidate
    for (let i = num; i <= target; i++) {
      for (let combination of dp[i - num]) {
        dp[i].push([...combination, num]);
      }
    }
  }

  return dp[target];
};
