/**
 * @param {number[]} nums
 * @return {number[][]}
 */
/// TC: TLE / SC: O(n)
// var threeSum = function(nums) {
//     const result = [];
//     const memo = {};

//     for (let i = 0; i < nums.length; i++) {
//         for (let j = 0; j < nums.length; j++) {
//             for (let k = 0; k < nums.length; k++) {
//                 if (i === k || i === j || j === k) continue;
//                 const comb = [nums[i], nums[j], nums[k]].sort((a, b) => a - b).join(",");

//                 if (memo[comb]) continue;
//                 if (!memo[comb]) memo[comb] = true;
//                 const sum = nums[i] + nums[j] + nums[k];
//                 if (sum === 0) result.push([nums[i], nums[j], nums[k]]);
//             }
//         }
//     }

//     return result;
// };

// TC: O(n^2) / SC: O(1)
var threeSum = function (nums) {
  const result = [];

  nums.sort((a, b) => a - b);

  for (let i = 0; i < nums.length; i++) {
    if (i > 0 && nums[i] === nums[i - 1]) continue;
    if (nums[i] > 0) break;

    let left = i + 1;
    let right = nums.length - 1;

    while (left < right) {
      const sum = nums[left] + nums[right];
      if (sum === -nums[i]) {
        result.push([nums[i], nums[left], nums[right]]);
        while (left < right && nums[left] === nums[left + 1]) left++;
        while (left < right && nums[right] === nums[right - 1]) right--;
        left++;
        right--;
      } else if (sum < -nums[i]) {
        left++;
      } else {
        right--;
      }
    }
  }

  return result;
};
