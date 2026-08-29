/**
 * @param {number[]} nums
 * @return {number}
 */

// TLE
// var maxSubArray = function(nums) {
//     if (nums.length <= 1) return nums[0];

//     const sum = (arr) => arr.reduce((acc, cur) => {
//         acc += cur;
//         return acc;
//     }, 0);

//     let total = -Infinity;
//     for (let i = 0; i < nums.length; i++) {
//         for (let j = i; j < nums.length; j++) {
//             const result = sum(nums.slice(i, j + 1));
//             total = Math.max(total, result);
//         }
//     }

//     return total;
// };

// TLE
// var maxSubArray = function(nums) {
//     if (nums.length <= 1) return nums[0];

//     let total = -Infinity;
//     for (let i = 0; i < nums.length; i++) {
//         let acc = 0;
//         for (let j = i; j < nums.length; j++) {
//             acc += nums[j];
//             total = Math.max(total, acc);
//         }
//     }

//     return total;
// };

// TC: O(n) / SC: O(1)
var maxSubArray = function (nums) {
  let total = nums[0];
  let acc = nums[0];

  for (let i = 1; i < nums.length; i++) {
    acc = Math.max(nums[i], acc + nums[i]); // 이전 누적값 선택 vs 현재값 선택 (카데인 알고리즘)
    total = Math.max(total, acc); // 최대 합산 값 갱신
  }

  return total;
};
