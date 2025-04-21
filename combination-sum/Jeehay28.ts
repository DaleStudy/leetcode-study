// Approach 2: Dynamic Programming
// ✅ Time Complexity: O(N * T * K)
// ✅ Space Complexity: O(T * K)
// N = Number of candidates, T = target, K = average number of combination for each dp[i]

function combinationSum(candidates: number[], target: number): number[][] {
  // candidates = [2, 3]
  // target = 5
  // dp = [
  //     [[]],         // dp[0]
  //     [],           // dp[1]
  //     [[2]],        // dp[2]
  //     [],           // dp[3]
  //     [[2, 2]],     // dp[4]
  //     []            // dp[5]
  // ];

  // dp = [
  //     [[]],         // dp[0]
  //     [],           // dp[1]
  //     [[2]],        // dp[2]
  //     [[3]],        // dp[3]
  //     [[2, 2]],     // dp[4]
  //     [[2, 3]]      // dp[5]
  // ];

  const dp: number[][][] = Array.from({ length: target + 1 }, () => []);
  // each element in dp is an independent array, and modifying one will not affect others.
  dp[0] = [[]];

  for (const candidate of candidates) {
    for (let num = candidate; num <= target; num++) {
      for (const combination of dp[num - candidate]) {
        dp[num].push([...combination, candidate]);
      }
    }
  }

  return dp[target];
}

// Approach 1: DFS + Backtracking (Recursive)
// ✅ Time Complexity: O(N^(T / min))
// ✅ Space Complexity: O(K + target / min)
// If target = 7 and smallest number is 2, recursion can go up to  7 / 2 = levels deep
// N = number of candidates, T = target value, K = total number of valid combination found

// function combinationSum(candidates: number[], target: number): number[][] {
//   // input:
//   // 1) an array of distinct integers
//   // 2) a target integer

//   // output:
//   // a list of all unique combinations of candinates where the chosen numbers sum to target(in any order)
//   // duplicated numbers allowed

//   let result: number[][] = [];
//   let nums: number[] = [];

//   const dfs = (start: number, total: number) => {
//     if (total > target) {
//       return;
//     }

//     if (total === target) {
//       result.push([...nums]);
//       return;
//     }

//     for (let i = start; i < candidates.length; i++) {
//       if (total + nums[i] <= target) {
//         nums.push(candidates[i]);
//         dfs(i, total + candidates[i]);
//         nums.pop(); // backtrack
//       }
//     }
//   };

//   dfs(0, 0);

//   return result;
// }
