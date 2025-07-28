/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function (nums) {
  const countMap = new Map();

  for (let i = 0; i < nums.length; i++) {
    const key = nums[i];
    if (countMap.has(key)) {
      const value = countMap.get(key);
      if (value === 1) {
        return true;
      }
      countMap.set(key, value + 1);
    } else {
      countMap.set(key, 1);
    }
  }

  return false;
};
