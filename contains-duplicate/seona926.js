/**
 * @param {number[]} nums
 * @return {boolean}
 */
let containsDuplicate = function (nums) {
  let counts = {};

  return nums.some((num) => {
    if (counts[num] === undefined) {
      counts[num] = 1;
      return false;
    } else {
      return true;
    }
  });
};
