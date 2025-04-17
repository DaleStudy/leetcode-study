// Approach 2: DFS with Memoization
// 🗓️ 2025-04-06
// ⏳ Time Complexity: O(n)
// 💾 Space Complexity: O(n)

function climbStairs(n: number): number {
  const memo = new Map<number, number>();

  const dfs = (step: number) => {
    if (step > n) return 0;
    if (step === n) return 1;
    if (memo.has(step)) return memo.get(step);

    const result = dfs(step + 1) + dfs(step + 2);
    memo.set(step, result);
    return result;
  };

  return dfs(0);
}


// Approach 1: DFS (depth-first search)
// ❌ Time Limit Exceeded (TLE) error!
// ⏳ Time Complexity: O(2^n)
// 💾 Space Complexity: O(n)
// The maximum depth of the recursive call stack is n, because we go from step = 0 to step = n.

// function climbStairs(n: number): number {
//   // 1 -> 1 -> 1
//   // 1 -> 2
//   // 2 -> 1

//   const dfs = (step: number) => {
//     // reach the top
//     if (step > n) return 0;
//     if (step === n) return 1;

//     return dfs(step + 1) + dfs(step + 2);
//   };

//   return dfs(0);
// }
