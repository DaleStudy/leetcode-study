// 시간 복잡도: O(n)
// 공간 복잡도: O(n)

/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function (nums) {
  const set = new Set(nums);
  if (set.size < nums.length) return true;
  else return false;
};
