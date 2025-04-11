// Approach 2
// 🗓️ 2025-04-08
// ⏳ Time Complexity: O(n + n) = O(n)
// 💾 Space Complexity: O(1)
// result: required output → not counted
// before, after: two scalar variables → O(1)
// So, the total extra space is O(1)

function productExceptSelf(nums: number[]): number[] {
  const result: number[] = new Array(nums.length).fill(1);
  let before = 1;
  let after = 1;

  for (let i = 0; i < nums.length - 1; i++) {
    before *= nums[i];
    result[i + 1] *= before;
  }

  for (let i = nums.length - 1; i > 0; i--) {
    after *= nums[i];
    result[i - 1] *= after;
  }
  return result;
}


// Approach 1
// 🗓️ 2025-04-08
// ⏳ Time Complexity: O(n + n + n) = O(n)
// 💾 Space Complexity: O(n + n) = O(n)

// When we analyze space complexity,
// we only count extra space used in addition to the input and required output.
// ✅ before → O(n) extra
// ✅ after → O(n) extra
// 🚫 result is the output, so it’s not counted toward space complexity

// function productExceptSelf(nums: number[]): number[] {
//   // nums: an array of size n
//   // before: nums[0], nums[1].., nums[i-2], nums[i-1]
//   // after: nums[i+1], nums[i+2],..., nums[n-1]

//   // input: [1, 2, 3, 4]
//   // before: [1, 1, 2, 6]
//   // after: [24, 12, 4, 1]
//   // product: [24, 12, 8, 6]

//   const before = new Array(nums.length).fill(1);
//   const after = new Array(nums.length).fill(1);
//   const result: number[] = [];

//   for (let i = 0; i < nums.length - 1; i++) {
//     before[i + 1] = before[i] * nums[i];
//   }

//   for (let i = nums.length - 1; i > 0; i--) {
//     after[i - 1] = after[i] * nums[i];
//   }

//   for (let i = 0; i < nums.length; i++) {
//     result[i] = before[i] * after[i];
//   }

//   return result;
// }
