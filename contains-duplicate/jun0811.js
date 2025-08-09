/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function (nums) {
  const count = [];
  let res = false;

  for (const num of nums) {
    if (count[num]) {
      res = true;
      break;
    } else {
      count[num] = 1;
    }
  }
  return res;
};
