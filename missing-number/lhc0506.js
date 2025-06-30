/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
  const n = nums.length;
  const array = new Array(n).fill(false);

  for (let i = 0; i < n; i++) {
      array[nums[i]] = true;
  }

  const index = array.findIndex(item => item === false);
  return index === -1 ? n : index;
};

// 시간 복잡도: O(n)
// 공간 복잡도: O(n)
