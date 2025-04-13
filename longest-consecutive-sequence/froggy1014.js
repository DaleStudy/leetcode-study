/**
 * @param {number[]} nums
 * @return {number}
 */

// 시간복잡도: O(n)
var longestConsecutive = function (nums) {
  let longest = 0;

  let set = new Set(nums);

  for (let num of nums) {
    if (set.has(num - 1)) {
      continue;
    }

    let count = 1;
    let currentNum = num;

    while (set.has(currentNum + 1)) {
      count++;
      currentNum++;
    }
    longest = Math.max(longest, count);
  }
  return longest;
};

console.log(longestConsecutive([100, 4, 200, 1, 3, 2])); // 4
console.log(longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])); // 9
console.log(longestConsecutive([1, 0, 1, 2])); // 3
