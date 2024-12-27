// Time complexity: O(nlogn)
// Space complexity: O(n)

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  const n = nums.length;

  const mappedNums = nums.map((num, i) => [num, i]);
  mappedNums.sort((a, b) => a[0] - b[0]);

  let left = 0;
  let right = n - 1;

  while (left < right) {
    const sum = mappedNums[left][0] + mappedNums[right][0];

    if (sum > target) {
      right--;
      continue;
    }

    if (sum < target) {
      left++;
      continue;
    }

    return [mappedNums[left][1], mappedNums[right][1]];
  }
};
