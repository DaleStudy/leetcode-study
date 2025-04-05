// Approach 3
// ⏳ Time Complexity: O(n) ✅ 
// 💾 Space Complexity: O(n)

function longestConsecutive(nums: number[]): number {
  if (nums.length === 0) return 0;

  const numSet = new Set<number>(nums);
  // The Set stores O(n) numbers.
  let longest = 0;

  for (const num of numSet) {
    if (!numSet.has(num - 1)) {
        // Set.has() operation runs in O(1) average time.
      let size = 1;

      while (numSet.has(num + size)) {
        size += 1;
      }

      longest = Math.max(longest, size);
    }
  }

  return longest;
}


// Approach 2
// ⏳ Time Complexity: O(n * log n)
// 💾 Space Complexity: O(1)

// function longestConsecutive(nums: number[]): number {
//   if (nums.length === 0) {
//     return 0;
//   }

//   nums.sort((a, b) => a - b);
//   // Sorting takes O(n * log n) time.
//   // Sorting is in-place -> O(1) extra space

//   let longest = 0;

//   let size = 1;

//   for (let i = 0; i < nums.length - 1; i++) {
//     if (nums[i] === nums[i + 1]) {
//       continue;
//     }

//     if (nums[i] + 1 === nums[i + 1]) {
//       size += 1;
//     } else {
//       longest = Math.max(longest, size);
//       size = 1;
//     }
//   }

//   longest = Math.max(longest, size);

//   return longest;
// }


// Approach 1
// ❌ Time Limit Exceeded!
// ⏳ Time Complexity: O(n^3)
// 💾 Space Complexity: O(1)

// function longestConsecutive(nums: number[]): number {
//     let longest = 0;

//     for (const num of nums) {
//         let size = 1;
//         while (nums.includes(num + size)) {
//             size += 1;
//         }

//         longest = Math.max(longest, size);
//     }

//     return longest;
// }


