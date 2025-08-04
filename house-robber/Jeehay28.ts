// Approach 4: Dynamic Programming with Two Variables
// ⏳ Time Complexity: O(n)
// 💾 Space Complexity: O(1) ✅

function rob(nums: number[]): number {
  let prev = 0, beforePrev = 0;

  for (const num of nums) {
    const current = Math.max(num + beforePrev, prev);
    beforePrev = prev;
    prev = current;
  }

  return prev;
}


// Approach 3: Dynamic Programming with a DP Array
// ⏳ Time Complexity: O(n)
// 💾 Space Complexity: O(n)

// function rob(nums: number[]): number {

//     //     dp = [0, 1, 2, 4, 4]
//     // robbing      h1 h2 h3 h4
//     const dp = new Array(nums.length + 1).fill(0);
//     dp[1] = nums[0];

//     for(let i=2; i<=nums.length; i++) {

//         dp[i] = Math.max(nums[i-1] + dp[i-2], dp[i-1]);
//         // nums[i-1]: the current house's money
//         // dp[i-2]: the max sum before the previous house (if robbing current house)
//         // dp[i-1]: the max sum up to the previous house (if robbing current house)
//     }

//     return dp[nums.length];
// };


// Approach 2: Recursive DFS with Memoization
// ⏳ Time Complexity: O(n)
// 💾 Space Complexity: O(n)

// function rob(nums: number[]): number {
//   let memo = new Map<number, number>();

//   const dfs = (start: number) => {
//     if (start >= nums.length) {
//       return 0;
//     }

//     if (memo.has(start)) {
//       return memo.get(start);
//     }

//     memo.set(start, Math.max(nums[start] + dfs(start + 2)!, dfs(start + 1)!));
//     // 👈 the exclamation mark tells TS “I’m sure it’s not undefined”
//     return memo.get(start);
//   };

//   return dfs(0)!;
// }


// Approach 1: Recursive DFS (Brute Force)
// ❌ Time Limit Exceeded!
// ⏳ Time Complexity: O(2^n)
// 💾 Space Complexity: O(n)
// The max call stack depth is n (in the worst case where you always call dfs(start + 1)).

// function rob(nums: number[]): number {
//   // F(nums) = MAX(nums[0] + F(nums[2:]), F(nums[1:]))
//   // F(start) = MAX(nums[start] + F(start + 2), F(start + 1))

//   const dfs = (start: number) => {
//     if (start >= nums.length) {
//       return 0;
//     }
//     return Math.max(nums[start] + dfs(start + 2), dfs(start + 1));
//   };

//   return dfs(0);
// }

