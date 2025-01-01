// 시간 복잡도: O(n)
// 공간 복잡도: O(n)

/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
  const numSet = new Set(nums);

  for (let i = 0; i <= nums.length; i++) {
    if (!numSet.has(i)) {
      return i;
    }
  }
};

