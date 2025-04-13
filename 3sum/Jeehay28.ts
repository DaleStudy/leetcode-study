// Approach 3
// 🗓️ 2025-04-12
// ⏳ Time Complexity: O(n log n) + O(n^2) = O(n^2)
// 💾 Space Complexity: O(1) (excluding output)

function threeSum(nums: number[]): number[][] {

    nums.sort((a, b) => a - b); // O(n log n)
    let result: number[][] = [];

    for (let i = 0; i < nums.length; i++) {

        if (i > 0 && nums[i - 1] == nums[i]) continue; // skip duplicate i

        let low = i + 1, high = nums.length - 1;
        // two-pointer scan (low and high) -> takes up to O(n) time per iteration
        while (low < high) {
            const threeSum = nums[i] + nums[low] + nums[high];
            if (threeSum < 0) {
                low += 1;
            } else if (threeSum > 0) {
                high -= 1;
            } else {
                result.push([nums[i], nums[low], nums[high]]);

                while (low < high && nums[low] === nums[low + 1]) low += 1 // skip duplicate low
                while (low < high && nums[high] === nums[high - 1]) high -= 1 // skip duplicate high

                low += 1;
                high -= 1;

            }
        }
    }
    return result
}


// Approach 2
// 🗓️ 2025-04-11
// ❌ Time Limit Exceeded 313 / 314 testcases passed
// ⏳ Time Complexity: O(n^2)
// 💾 Space Complexity: O(n^2)

// function threeSum(nums: number[]): number[][] {
//   const result: number[][] = [];
//   const triplets = new Set<string>();

//   for (let i = 0; i < nums.length - 2; i++) {
//     const seen = new Set<number>();
//     for (let j = i + 1; j < nums.length; j++) {
//       const twoSum = nums[i] + nums[j];
//       if (seen.has(-twoSum)) {
//         const triplet = [nums[i], nums[j], -twoSum].sort((a, b) => a - b); // O(log 3) = O(1)
//         const key = triplet.join(",");
//         if (!triplets.has(key)) {
//           triplets.add(key);
//           result.push(triplet);
//         }
//       }
//       seen.add(nums[j]);
//     }
//   }
//   return result;
// }


// Approach 1
// 🗓️ 2025-04-11
// ❌ Time Limit Exceeded!
// ⏳ Time Complexity: O(n^3)
// 💾 Space Complexity: O(n^2)

// function threeSum(nums: number[]): number[][] {

//     let triplets = new Set<string>();
//     let result: number[][] = [];

//     // const set = new Set();
//     // set.add([1, 2, 3]);
//     // set.add([1, 2, 3]);
//     // console.log(set); // contains BOTH arrays
//     // Set(2) { [ 1, 2, 3 ], [ 1, 2, 3 ] }

//     for (let i = 0; i < nums.length - 2; i++) {
//         for (let j = i + 1; j < nums.length - 1; j++) {
//             for (let k = j + 1; k < nums.length; k++) {
//                 if (nums[i] + nums[j] + nums[k] === 0) {
//                     const triplet = [nums[i], nums[j], nums[k]].sort((a, b) => a - b);
//                     const key = triplet.join(",");
//                     if (!triplets.has(key)) {
//                         triplets.add(key);
//                         result.push(triplet)
//                     }
//                 }
//             }
//         }
//     }

//     return result;
// };
