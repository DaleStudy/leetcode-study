// 🚀 Greedy approach: much more efficient than the recursive approach
// Time Complexity: O(n)
// Space Complexity: O(1), No extra memory used

/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canJump = function (nums) {
  // ➡️ The farthest position you can reach from any of the previous indices you have already visited.
  let farthest = 0;

  for (let i = 0; i < nums.length; i++) {
    // You cannot reach this position even with your farthest jump value.
    if (i > farthest) return false;

    // Compare current maximum jump with the previous maximum.
    farthest = Math.max(farthest, nums[i] + i);

    // Check if you can reach the last index with the current farthest jump.
    if (farthest >= nums.length - 1) return true;
  }
  return false;
};


/**
 * @param {number[]} nums
 * @return {boolean}
 */

// Time Complexity: O(n)
// Space Complexity: O(n)
var canJump = function (nums) {
  let lastIndex = nums.length - 1;

  // Initialize memoization array to track visited indices
  let memo = new Array(nums.length).fill(undefined);

  const dfs = (i) => {
    // Base case: if we've reached or surpassed the last index, return true
    if (i >= lastIndex) return true;

    // If the current index has already been visited, return the stored result
    if (memo[i] !== undefined) return memo[i];

    // Calculate the farthest position that can be reached from the current index
    let maxJump = Math.min(nums[i] + i, lastIndex);

    for (let j = i + 1; j <= maxJump; j++) {
      if (dfs(j)) {
        memo[i] = true;
        return true;
      }
    }

    memo[i] = false;
    return false;
  };

  return dfs(0);
};


// 🌀 recursive approach
// ⚠️ Time Complexity: O(2^n) - Exponential due to recursive branching without memoization
// 🔵 Space Complexity: O(n) - Recursive call stack depth

/**
 * Check if you can jump to the last index from the first index.
 * @param {number[]} nums - Array where nums[i] is the max jump length from position i.
 * @return {boolean} True if you can reach the last index, otherwise false.
 */

// var canJump = function (nums) {
//   const dfs = (start) => {
//     // Base Case: Reached the last index
//     if (start === nums.length - 1) {
//       return true;
//     }

//     // Recursive Case: Try all possible jumps
//     for (let i = 1; i <= nums[start]; i++) {
//       // Example with nums = [2, 3, 1, 1, 4]:
//       // start = 1, nums[1] = 3 (can jump 1, 2, or 3 steps)
//       // Possible calls:
//       //   dfs(1 + 1) -> check from index 2
//       //   dfs(1 + 2) -> check from index 3
//       //   dfs(1 + 3) -> reached the last index (success)

//       if (dfs(start + i)) {
//         return true;
//       }
//     }

//     return false; // cannot reach the last index
//   };

//   return dfs(0);
// };

