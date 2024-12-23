// Time complexity: O(n^2)
// Space complexity: O(n)

/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function (nums) {
  const sumsDict = new Set();
  const sortedNums = nums.toSorted((a, b) => a - b);

  const n = nums.length;

  for (let i = 0; i < n - 2; i++) {
    let left = i + 1;
    let right = n - 1;
    const fixed = sortedNums[i];

    const targetSum = 0 - fixed;

    while (left < right) {
      const currentSum = sortedNums[left] + sortedNums[right];

      if (currentSum < targetSum) {
        left++;
      } else if (currentSum > targetSum) {
        right--;
      } else {
        const key = [fixed, sortedNums[left], sortedNums[right]];
        sumsDict.add(key.join(","));
        left++;
        right--;
      }
    }
  }

  return Array.from(sumsDict).map((nums) => nums.split(",").map(Number));
};
